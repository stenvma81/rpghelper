from flask import session
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from utils.csrf_utils import get_csrf_token
from db.db import db


def get_user_by_username(username):
    try:
        sql = text("""
            SELECT *
            FROM users
            WHERE username = :username
        """)
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()
        return user
    except Exception as e:
        raise Exception(f"Error fetching user details: {str(e)}")


def login_user(username, password):
    user_data = get_user_by_username(username)

    if not user_data:
        raise Exception("Invalid credentials. Try again.")
    
    try:
        sql = text("""
            SELECT password
            FROM users
            WHERE username = :username
        """)
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()

        if user and check_password_hash(user[0], password):
            session["user_id"] = user_data[0]
            session["username"] = username
            session["role"] = user_data[3]
            session["csrf_token"] = get_csrf_token()
            return True
        
        return False

    except Exception as e:
        raise Exception(f"Error fetching user details: {str(e)}")
    

def register_user(username, password, role):
    hashed_password = generate_password_hash(password)

    try:
        sql = text("""
        INSERT INTO users (username, password, role)
        VALUES (:username, :password, :role)
        """)
        db.session.execute(sql, {"username": username, "password": hashed_password, "role": role})
        db.session.commit()

    except IntegrityError:
        db.session.rollback()
        raise Exception("Username already taken.")
    
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error registering user: {str(e)}")


def logout_user():
    keys_to_delete = ["user_id", "username", "role", "csrf_token"]
    for key in keys_to_delete:
        try:
            del session[key]
        except KeyError:
            pass

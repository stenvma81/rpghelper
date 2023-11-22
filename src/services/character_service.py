import os
from flask import abort, request, session
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from db.db import db


def get_all_characters():
    try:
        sql = text("""
            SELECT *
            FROM characters
        """)
        result = db.session.execute(sql)
        character_list = result.fetchall()
        return character_list
    except Exception as e:
        raise Exception(f"Error fetching all characters: {str(e)}")


def get_characters_by_user_id(user_id):
    try:
        sql = text("""
            SELECT *
            FROM characters
            WHERE user_id = :user_id
        """)
        result = db.session.execute(sql, {"user_id": user_id})
        character_list = result.fetchall()
        return character_list
    except Exception as e:
        raise Exception(f"Error fetching character details: {str(e)}")
    

def get_character_by_character_id(character_id):
    try:
        sql = text("""
            SELECT *
            FROM characters
            WHERE character_id = :character_id
        """)
        result = db.session.execute(sql, {"character_id": character_id})
        character = result.fetchone()
        return character
    except Exception as e:
        raise Exception(f"Error fetching character details: {str(e)}")
    

def create_character(name, health, armor_class, user_id):
    try:
        sql = text("""
        INSERT INTO characters (name, health, armor_class, user_id)
        VALUES (:name, :health, :armor_class, :user_id)
        """)
        db.session.execute(sql, {
            "name": name, 
            "health": health, 
            "armor_class": armor_class, 
            "user_id": user_id
            })
        db.session.commit()
    
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error creating new character: {str(e)}")
    

def modify_character(character_id, name, health, armor_class):
    try:
        sql = text("""
            UPDATE characters
            SET name = :name, health = :health, armor_class = :armor_class
            WHERE character_id = :character_id
        """)
        db.session.execute(sql, {
            "character_id": character_id,
            "name": name,
            "health": health,
            "armor_class": armor_class,
            })
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error modifying character: {str(e)}")


def delete_character(character_id):
    try:
        sql = text("""
        DELETE FROM characters WHERE character_id = :character_id
        """)
        db.session.execute(sql, {"character_id": character_id})
        db.session.commit()
    
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Error deleting character: {str(e)}")


def get_character_form_data():
    name = request.form.get('name')

    health_string = request.form.get('health')
    health = int(health_string) if health_string else None

    armor_class_string = request.form.get('armor_class')
    armor_class = int(armor_class_string) if armor_class_string else None

    return name, health, armor_class


def character_form_check_input(name, health, armor_class, error):
    if not name or not health or not armor_class:
        error = "All fields are required!"
    elif health < 1:
        error = "The character must have at least 1 point of health."
    elif armor_class < 0:
        error = "Armor class can't be under 0."

    return error
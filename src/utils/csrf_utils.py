from flask import session, request, abort
import os


def get_csrf_token():
    if "csrf_token" not in session:
        create_csrf_token()
    return session["csrf_token"]


def create_csrf_token():
    session["csrf_token"] = os.urandom(16).hex()


def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
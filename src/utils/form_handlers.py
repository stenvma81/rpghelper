from flask import request

class CharacterHandlers:
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


class UserHandlers:
    def get_register_form_data():
        username = request.form.get('username')
        role = request.form.get('role')
        password_a = request.form.get('password_a')
        password_b = request.form.get('password_b')

        return username, role, password_a, password_b


    def get_login_form_data():
        username = request.form.get('username')
        password = request.form.get('password')

        return username, password


    def register_form_check_input(username, password_a, password_b, error):
        if not username or not password_a or not password_b:
            error = "All fields are required!"
        elif password_a != password_b:
            error = "Passwords do not match"
        elif len(password_a) < 4:
            error = "Password should be at least 4 characters long"

        return error


    def login_form_check_input(username, password):
        error = None

        if not username or not password:
            error = "Both username and password are required"
            return error
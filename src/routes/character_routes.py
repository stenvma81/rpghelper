from flask import render_template, request, redirect, url_for, session
import logging
from services import character_service, user_service
from utils.form_handlers import CharacterHandlers


def character_routes(app):
    

    @app.route('/characters/list', methods=['GET'])
    def my_characters_route():
        error = None
        user_id = session.get('user_id')

        try:
            character_list = character_service.get_characters_by_user_id(user_id)
        except Exception as e:
                error = "Character list fetch failed."
                logging.error(f"Error occurred: {str(e)}")

        csrf_token = user_service.get_csrf_token()
        return render_template('my_characters.html', character_list=character_list, error=error, csrf_token=csrf_token)


    @app.route('/characters/create', methods=['GET'])
    def create_character_route_get():
        error = None

        csrf_token = user_service.get_csrf_token()
        return render_template('create_character.html', error=error, csrf_token=csrf_token, character=None)


    @app.route('/characters/create', methods=['POST'])
    def create_character_route_post():
        error = None

        name, health, armor_class = CharacterHandlers.get_character_form_data()
        user_id = session.get('user_id')

        error = CharacterHandlers.character_form_check_input(name, health, armor_class, error)

        if not error:
            try:
                character_service.create_character(name, health, armor_class, user_id)
                return redirect(url_for('my_characters_route'))
            except Exception as e:
                error = "Character creation failed."
                logging.error(f"Error occurred: {str(e)}")
    

    @app.route('/characters/modify/<int:character_id>', methods=['GET'])
    def modify_character_get(character_id):
        error = None
        csrf_token = user_service.get_csrf_token()

        character = character_service.get_character_by_character_id(character_id)

        if character is None:
            error = "Character not found"
            return redirect('my_characters_route', error=error, csrf_token=csrf_token)
        else:
            return render_template('modify_character.html', error=error, character_id=character_id, character=character, csrf_token=csrf_token)


    @app.route('/characters/modify/<int:character_id>', methods=['GET'])
    def modify_character_post(character_id):
        try:
            name, health, armor_class = CharacterHandlers.get_character_form_data()
            character_service.modify_character(character_id, name, health, armor_class)
        except Exception as e:
            error = "Character modifying failed."
            logging.error(f"Error occurred: {str(e)}")

        return redirect(url_for('my_characters_route'))


    @app.route('/characters/delete/<int:character_id>', methods=['POST'])
    def delete_character(character_id):
        error = None

        try:
            character_list = character_service.delete_character(character_id)
        except Exception as e:
                error = "Character deletion failed."
                logging.error(f"Error occurred: {str(e)}")

        return redirect(url_for('my_characters_route', error=error))
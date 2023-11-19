from flask import render_template, request, redirect, url_for, session
import logging
from components import characters, users


def character_routes(app):
    

    @app.route('/characters/list', methods=['GET'])
    def my_characters_route():
        error = None
        user_id = session.get('user_id')

        try:
            character_list = characters.get_characters_by_user_id(user_id)
        except Exception as e:
                error = "Character list fetch failed."
                logging.error(f"Error occurred: {str(e)}")

        csrf_token = users.get_csrf_token()
        return render_template('my_characters.html', character_list=character_list, error=error, csrf_token=csrf_token)


    @app.route('/characters/create', methods=['GET', 'POST'])
    def create_character_route():
        error = None

        if request.method == 'POST':
            name, health, armor_class = characters.get_character_form_data()
            user_id = session.get('user_id')

            error = characters.character_form_check_input(name, health, armor_class, error)

            if not error:
                try:
                    characters.create_character(name, health, armor_class, user_id)
                    return redirect(url_for('my_characters_route'))
                except Exception as e:
                    error = "Character creation failed."
                    logging.error(f"Error occurred: {str(e)}")

        csrf_token = users.get_csrf_token()
        return render_template('create_character.html', error=error, csrf_token=csrf_token, character=None)
    

    @app.route('/characters/modify/<int:character_id>', methods=['GET', 'POST'])
    def modify_character(character_id):
        error = None
        print("request method: ", request.method)

        character = characters.get_character_by_character_id(character_id)
        if character is None:
            error = "Character not found"
            return render_template('modify_character.html', error=error, character=None)

        if request.method == 'POST':
            try:
                name, health, armor_class = characters.get_character_form_data()
                characters.modify_character(character_id, name, health, armor_class)

                return redirect(url_for('my_characters_route'))
            except Exception as e:
                error = "Character modifying failed."
                logging.error(f"Error occurred: {str(e)}")

        return render_template('modify_character.html', error=error, character_id=character_id, character=character)


    @app.route('/characters/delete/<int:character_id>', methods=['POST'])
    def delete_character(character_id):
        error = None

        try:
            character_list = characters.delete_character(character_id)
        except Exception as e:
                error = "Character deletion failed."
                logging.error(f"Error occurred: {str(e)}")

        return redirect(url_for('my_characters_route'))
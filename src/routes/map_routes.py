from flask import render_template, redirect, url_for, session
import logging
from services import user_service, character_service


def map_routes(app):
    

    @app.route('/map', methods=['GET'])
    def map_route_get():
        error = None
        user_id = session.get('user_id')

        try:
            character_list = character_service.get_characters_by_user_id(user_id)
        except Exception as e:
                error = "Character list fetch failed."
                logging.error(f"Error occurred: {str(e)}")

        csrf_token = user_service.get_csrf_token()
        return render_template('map.html', error=error, character_list=character_list, csrf_token=csrf_token)
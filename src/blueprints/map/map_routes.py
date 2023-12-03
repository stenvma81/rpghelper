from flask import Blueprint, session, render_template
from services import character_service, user_service
from . import map_blueprint
import logging


@map_blueprint.route('/map', methods=['GET'])
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
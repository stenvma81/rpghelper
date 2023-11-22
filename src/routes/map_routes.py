from flask import render_template, redirect, url_for, session
from services import user_service


def map_routes(app):
    

    @app.route('/map', methods=['GET'])
    def map_route_get():

        csrf_token = user_service.get_csrf_token()
        return render_template('map.html', error=None, csrf_token=csrf_token)
from flask import render_template, request, redirect, url_for, session
import logging
from services import user_service
from utils.form_handlers import UserHandlers
from utils.csrf_utils import get_csrf_token


def auth_routes(app):


    @app.route('/')
    def index_route():
        return render_template('index.html')


    @app.route('/login', methods=['GET'])
    def login_route_get():
        error = session.pop('error', None)

        csrf_token = get_csrf_token()
        return render_template('login.html', error=error, csrf_token=csrf_token)
    

    @app.route('/login', methods=['POST'])
    def login_route_post():
        username, password = UserHandlers.get_login_form_data()

        error = UserHandlers.login_form_check_input(username, password)

        if not error:
            try:
                if user_service.login_user(username, password):
                    return redirect(url_for('index_route'))
                else:
                    session['error'] = "Invalid credentials"
                    return redirect(url_for('login_route_get'))

            except Exception as e:
                session['error'] = "Login failed."
                logging.error(f"Error occurred: {str(e)}")
                return redirect(url_for('login_route_get'))
    

    @app.route('/register', methods=['GET'])
    def register_route_get():
        error = None

        csrf_token = get_csrf_token()
        return render_template('register.html', error=error, csrf_token=csrf_token)


    @app.route('/register', methods=['POST'])
    def register_route_post():
        error = None

        username, role, password_a, password_b = UserHandlers.get_register_form_data()

        error = UserHandlers.register_form_check_input(username, password_a, password_b, error)

        if not error:
            try:
                user_service.register_user(username, password_a, role)
                user_service.login_user(username, password_a)
                return redirect(url_for('index_route'))
            except Exception as e:
                error = "Failed to register new user"
                logging.error(f"Error occurred: {str(e)}")
    
    
    @app.route('/logout')
    def logout_route():
        user_service.logout_user()
        return redirect(url_for('index_route'))
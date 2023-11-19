from flask import render_template, request, redirect, url_for, session
import logging
from components import users


def auth_routes(app):


    @app.route('/')
    def index_route():
        return render_template('index.html')


    @app.route('/login', methods=['GET', 'POST'])
    def login_route():
        error = None

        if request.method == 'POST':
            username, password = users.get_login_form_data()

            error = users.login_form_check_input(username, password)

            if not error:
                try:
                    if users.login_user(username, password):
                        return redirect(url_for('index_route'))
                    else:
                        error = "Invalid credentials"

                except Exception as e:
                    error = "Login failed."
                    logging.error(f"Error occurred: {str(e)}")

        csrf_token = users.get_csrf_token()
        return render_template('login.html', error=error, csrf_token=csrf_token)
    

    @app.route('/register', methods=['GET', 'POST'])
    def register_route():
        error = None

        if request.method == 'POST':
            username, role, password_a, password_b = users.get_register_form_data()

            error = users.register_form_check_input(username, password_a, password_b, error)

            if not error:
                try:
                    users.register_user(username, password_a, role)
                    users.login_user(username, password_a)
                    return redirect(url_for('index_route'))
                except Exception as e:
                    error = "Failed to register new user"
                    logging.error(f"Error occurred: {str(e)}")

        csrf_token = users.get_csrf_token()
        return render_template('register.html', error=error, csrf_token=csrf_token)
    
    
    @app.route('/logout')
    def logout_route():
        users.logout_user()
        return redirect(url_for('index_route'))
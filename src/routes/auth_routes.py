def auth_routes(app):

    @app.route('/')
    def index_route():
        return "This app is running fine"
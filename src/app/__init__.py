from dotenv import load_dotenv
import os
load_dotenv()

from flask import Flask
from flask_migrate import Migrate
from routes.auth_routes import auth_routes
from db.db import db
from utils.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print(app.config['SQLALCHEMY_DATABASE_URI'])  # Debugging line
    db.init_app(app)
    # migrate = Migrate(app, db)
    auth_routes(app)

    return app
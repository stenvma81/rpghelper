from flask import Flask, render_template
from dotenv import load_dotenv
from flask_migrate import Migrate

load_dotenv()

from utils.config import Config
from routes.auth_routes import auth_routes
from routes.character_routes import character_routes
from db.db import db
from models.user import User
from models.character import Character


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
auth_routes(app)
character_routes(app)

if __name__ == '__main__':
        app.run(debug=True)
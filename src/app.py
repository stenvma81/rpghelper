from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate

load_dotenv()

from utils.config import Config
from blueprints.map import map_blueprint
from blueprints.auth import auth_blueprint
from blueprints.character import character_blueprint
from db.db import db
from models.user_model import User
from models.character_model import Character


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(map_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(character_blueprint)

if __name__ == '__main__':
        app.run(debug=True)
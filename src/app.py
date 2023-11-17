from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

from utils.config import Config
from routes.auth_routes import auth_routes
from db.db import database


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
database.init_app(app)
auth_routes(app)

if __name__ == '__main__':
        app.run(debug=True)
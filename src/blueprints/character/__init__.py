from flask import Blueprint


character_blueprint = Blueprint('character_blueprint', __name__,
                          template_folder='templates')

from .character_routes import *
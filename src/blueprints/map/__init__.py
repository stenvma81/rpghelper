from flask import Blueprint


map_blueprint = Blueprint('map_blueprint', __name__,
                          template_folder='templates',
                          static_folder='static')

from .map_routes import *
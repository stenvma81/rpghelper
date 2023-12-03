from flask import Blueprint


auth_blueprint = Blueprint('auth_blueprint', __name__,
                          template_folder='templates')

from .auth_routes import *
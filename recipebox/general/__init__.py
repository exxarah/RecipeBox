from flask import Blueprint

general_bp = Blueprint(
    'general_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/general/static/'
)

from . import general

from flask import Blueprint

general_bp = Blueprint(
    'general_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='assets'
)

from . import general, ingredients, recipes

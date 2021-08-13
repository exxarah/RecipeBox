from flask import Blueprint

recipe_bp = Blueprint(
    'recipe_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/recipes/static/'
)

from . import ingredients, recipes

from flask import Blueprint, render_template
from recipebox.models.general import Ingredient

general_bp = Blueprint(
    'general_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='assets'
)

@general_bp.route('/hello')
def hello():
    return 'Hello World!'

@general_bp.route('/ingredient')
def ingredient():
    return render_template('ingredient_all.html', ingredients=Ingredient.query.all())

@general_bp.route('/ingredient/new')
def ingredient_new():
    return render_template('ingredient_new.html')

@general_bp.route('/recipe/<id>')
def recipe():
    return

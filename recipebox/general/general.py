from flask import Blueprint, render_template, url_for, request, redirect
from sqlalchemy import func
from recipebox.models.general import Ingredient
from recipebox import db

general_bp = Blueprint(
    'general_bp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='assets'
)

@general_bp.route('/hello/')
def hello():
    return 'Hello World!'

@general_bp.route('/ingredient/')
def ingredient():
    return render_template('ingredient_all.html', ingredients=Ingredient.query.all())

@general_bp.route('/ingredient/new/', methods=['GET', 'POST'])
def ingredient_new():
    if request.method == 'POST':
        ingredient = Ingredient(
            name=request.form["name"]
        )
        db.session.add(ingredient)
        db.session.commit()
        return redirect(url_for("general_bp.ingredient_id", id=ingredient.id))
    else:
        return render_template('ingredient_new.html')

@general_bp.route('/ingredient/<id>/')
def ingredient_id(id):
    return render_template('ingredient_all.html', ingredients=[Ingredient.query.get(id)])
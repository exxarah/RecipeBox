from flask import render_template, url_for, request, redirect
from recipebox.models.general import Ingredient
from recipebox import db
from . import general_bp


@general_bp.route('/ingredient/')
def ingredient():
    return render_template('ingredient_browse.html', browse_items=Ingredient.query.all())


@general_bp.route('/ingredient/new/', methods=['GET', 'POST'])
def ingredient_new():
    if request.method == 'POST':
        ingredient = Ingredient(
            name=request.form["name"]
        )
        db.session.add(ingredient)
        db.session.commit()
        return redirect(url_for("general_bp.ingredient_view", id=ingredient.id))
    else:
        return render_template('ingredient_new.html')


@general_bp.route('/ingredient/<id>/')
def ingredient_view(id):
        selected_ingredient = Ingredient.query.get(id)
        if selected_ingredient is None:
            return render_template('404_notfound.html')
        else:
            return render_template('ingredient_view.html', ingredient=selected_ingredient)

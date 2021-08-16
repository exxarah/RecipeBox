from flask import render_template, url_for, request, redirect
from recipebox.models.general import Ingredient
from recipebox import db
from . import recipe_bp

@recipe_bp.route('/ingredient/new/', methods=['GET', 'POST'])
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
from flask import render_template, url_for, request, redirect, jsonify
from recipebox.models.recipes import Ingredient
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
        return redirect(url_for("recipe_bp.recipe", id=ingredient.id))
    else:
        return render_template('new_ingredient.html')


@recipe_bp.route('/ingredient/search/<string>')
def ingredient_search(string):
    matching_ingredients = [ingredient.name for ingredient in Ingredient.search_name(string)]
    print(matching_ingredients)
    return jsonify(ingredients=matching_ingredients)

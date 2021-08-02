from flask import render_template, url_for, request, redirect
import sys
from recipebox.models.general import Recipe
from recipebox import db
from . import general_bp


@general_bp.route('/recipe/')
def recipe():
    selected_recipes = Recipe.query.all()
    return render_template('recipe_browse.html', recipes=selected_recipes)


@general_bp.route('/recipe/new/', methods=['GET', 'POST'])
def recipe_new():
    if request.method == 'POST':
        recipe = Recipe(
            name=request.form["name"]
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("general_bp.recipe_id", id=recipe.id))
    else:
        return render_template('recipe_new.html')


@general_bp.route('/recipe/<id>/')
def recipe_id(id):
    selected_recipe = Recipe.query.get(id)
    if selected_recipe is None:
        return render_template('404_notfound.html')
    else:
        return render_template('recipe_view.html', recipe=selected_recipe)

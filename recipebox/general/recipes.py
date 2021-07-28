from flask import render_template, url_for, request, redirect
from recipebox.models.general import Recipe
from recipebox import db
from . import general_bp


@general_bp.route('/recipe/')
def recipe():
    return render_template('recipe_all.html', ingredients=Recipe.query.all())


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


@general_bp.route('/recipe/<recipe_id>/')
def recipe_id(recipe_id):
    return render_template('recipe_all.html', ingredients=[Recipe.query.get(recipe_id)])

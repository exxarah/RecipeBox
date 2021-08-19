import os
import uuid

import flask
from flask import render_template, url_for, request, redirect, flash

from config import ALLOWED_EXTENSIONS
from recipebox.models.recipes import Recipe, Ingredient, RecipeIngredient, RecipeProcedure
from recipebox import db
from . import recipe_bp


@recipe_bp.route('/recipe/')
def recipe():
    selected_recipes = Recipe.query.all()
    return render_template('browse.html', browse_items=selected_recipes)


@recipe_bp.route('/recipe/new/', methods=['GET'])
def recipe_new_get():
    return render_template('new_recipe.html', ingredients=Ingredient.query.all())

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@recipe_bp.route('/recipe/new/', methods=['POST'])
def recipe_new_post():
    # Image validation first
    if 'recipe_image' not in request.files:
        flash('No image uploaded')
        return redirect(request.url)
    recipe_image = request.files['recipe_image']

    if recipe_image.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if not (recipe_image or allowed_file(recipe_image.filename)):
        flash('Please specify a valid image to upload.')
        return redirect(request.url)

    safe_filename = str(uuid.uuid4())
    safe_filename += '.' + recipe_image.filename.rsplit('.', 1)[1].lower()

    # File is now validated, lets save it
    recipe_image.save(os.path.join(flask.current_app.config['UPLOAD_FOLDER'], safe_filename))

    recipe = Recipe(
        name=request.form["recipe_name"],
        picture=safe_filename,
        cook_time=request.form["recipe_cooktime"]
    )

    ingredient = Ingredient.select(request.form.getlist("recipe_ingredients[]")[0])

    for i in range(len(request.form.getlist("recipe_amount[]"))):
        i = RecipeIngredient(
            recipe=recipe.id,
            ingredient=ingredient.id,
            quantity=request.form.getlist("recipe_amount[]")[i],
            unit=request.form.getlist("recipe_unit[]")[i]
        )
        recipe.ingredients.append(i)

    for i in range(len(request.form.getlist("recipe_procedure[]"))):
        i = RecipeProcedure(
            recipe=recipe.id,
            step=i+1,
            procedure=request.form.getlist("recipe_procedure[]")[i]
        )
        recipe.procedures.append(i)

    db.session.add(recipe)
    db.session.flush()
    db.session.commit()
    return redirect(url_for("recipe_bp.recipe_view", id=recipe.id))

@recipe_bp.route('/recipe/<id>/')
def recipe_view(id):
    selected_recipe = Recipe.query.get(id)
    if selected_recipe is None:
        return render_template('404_notfound.html')
    else:
        return render_template('view.html', recipe=selected_recipe)

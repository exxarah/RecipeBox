from flask import render_template, url_for, request, redirect
from recipebox.models.recipes import Recipe, Ingredient, RecipeIngredient
from recipebox import db
from . import recipe_bp


@recipe_bp.route('/recipe/')
def recipe():
    selected_recipes = Recipe.query.all()
    return render_template('browse.html', browse_items=selected_recipes)


@recipe_bp.route('/recipe/new/', methods=['GET', 'POST'])
def recipe_new():
    if request.method == 'POST':
        recipe = Recipe(
            name=request.form["name"]
        )
        # Instead of this, get a list of tuples of format (ingredient_id, amount, unit)
        for ingredient in request.form.getlist('ingredients'):
            print(ingredient)
            i = RecipeIngredient(
                recipe=recipe.id,
                ingredient=ingredient,
                quantity=100,
                unit="grams"
            )
            recipe.ingredients.append(i)
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("recipe_bp.recipe_view", id=recipe.id))
    else:
        return render_template('new_recipe.html', ingredients=Ingredient.query.all())


@recipe_bp.route('/recipe/<id>/')
def recipe_view(id):
    selected_recipe = Recipe.query.get(id)
    if selected_recipe is None:
        return render_template('404_notfound.html')
    else:
        return render_template('view.html', recipe=selected_recipe)

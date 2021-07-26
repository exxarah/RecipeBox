""" Data Models for General website content. """

from flask import current_app
import os
from recipebox import db

class Ingredient(db.Model):
    """
    Ingredient Model Data.

    Attributes:
        name (str): name of ingredient
        picture (str): path to picture
    """
    __tablename__ = "ingredient"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    picture  = db.Column(db.String(150), nullable=False)
    recipes = db.relationship('RecipeIngredient', backref="ingredient", lazy=True)

    def __init__(self, name):
        self.name = name
        self.picture = os.path.join(*[current_app.config['STATIC_DIR'], "ingredients", name + ".png"])


class Recipe(db.Model):
    """
    Recipe Model Data.

    Attributes:
        name (str): name of recipe
        picture (str): path to picture
        ingredients (RecipeIngredient): many to one relationship with RecipeIngredients
    """
    __tablename__ = "recipe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    picture = db.Column(db.String(150), nullable=False)
    ingredients = db.relationship('RecipeIngredient', backref="recipe", lazy=True)

    def __init__(self, name):
        self.name = name
        self.picture = os.path.join(*[current_app.config['STATIC_DIR'], "recipes", name + ".png"])

class RecipeIngredient(db.Model):
    """
    Recipe Ingredient Model Data.

    A specific ingredient entry in a recipe.

    Attributes:
        recipe_id: recipe this belongs to
        ingredient (Ingredient): ingredient to reference
        quantity (int): amount of the ingredient
        unit (str): unit of measurement
    """
    __tablename__ = "recipe_ingredient"
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(30), nullable=False)

    def __init__(self, recipe, ingredient, quantity, unit):
        self.recipe_id = recipe
        self.ingredient_id = ingredient
        self.quantity = quantity
        self.unit = unit

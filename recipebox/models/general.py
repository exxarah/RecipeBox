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
    name = db.Column(db.String(30))
    picture  = db.Column(db.String(150))

    def __init__(self, name):
        self.name = name
        self.picture = os.path.join(current_app.config['STATIC_DIR'], name + ".png")


class Recipe(db.Model):
    """
    Recipe Model Data.

    Attributes:
        name (str): name of recipe
        picture (str): path to picture
        ingredients (RecipeItem):
    """
    __tablename__ = "recipe"
    id = db.Column(db.Integer, primary_key=True)

class RecipeIngredient(db.Model):
    """
    Recipe Ingredient Model Data.

    A specific ingredient entry in a recipe.

    Attributes:
        ingredient (Ingredient): ingredient to reference
        quantity (int): amount of the ingredient
        unit (str): unit of measurement
    """
    __tablename__ = "recipe_ingredient"
    id = db.Column(db.Integer, primary_key=True)

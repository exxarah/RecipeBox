""" Data Models for General website content. """
import datetime

from flask import current_app
import os
from recipebox import db
from recipebox.models.auth import Like

tags = db.Table(
    'tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
)

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
    recipes = db.relationship('RecipeIngredient', backref="ingredient_object", lazy=True)

    def __init__(self, name):
        self.name = name
        self.picture = os.path.join(*[current_app.config['STATIC_DIR'], "ingredients.py", name + ".png"])

    @classmethod
    def search_name(cls, query):
        if not query or not isinstance(query, str):
            raise ValueError("Missing query arg as a string")
        search_query = "%{0}%".format(query)
        return cls.query.filter(cls.name.ilike(search_query)).all()

    @classmethod
    def select(cls, query):
        if not query or not isinstance(query, str):
            raise ValueError("Missing query arg as a string")
        ingredient = cls.query.filter(cls.name == query).first()
        # If we managed to select an ingredient, return it
        if ingredient:
            return ingredient
        # If we get here, we need to create a new ingredient and return it
        ingredient = Ingredient(
            name=query
        )
        db.session.add(ingredient)
        db.session.flush()
        return ingredient

class Recipe(db.Model):
    """
    Recipe Model Data.

    Attributes:
        name (str): name of recipe
        picture (str): path to picture
        cook_time (int): time to make, in minutes
        ingredients (RecipeIngredient): many to one relationship with RecipeIngredients
        procedures (RecipeProcedure): many to one relationship with RecipeProcedures
        poster (User): one to many relationship with Users
        likes (Like): many to one relationship with Likes
    """
    __tablename__ = "recipe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    picture = db.Column(db.String(150), nullable=False)
    cook_time = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    ingredients = db.relationship('RecipeIngredient', backref="recipe_object", lazy=True)
    procedures = db.relationship('RecipeProcedure', backref="recipe_object", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    likes = db.relationship('Like', backref="recipe_object", lazy=True)
    ratings = db.relationship('Rating', backref="recipe_object", lazy=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery', backref=db.backref('recipes', lazy=True))

    def __init__(self, name, picture, cook_time):
        self.name = name
        self.picture = picture
        self.cook_time = cook_time
        self.user_id = 0
        self.date_created = datetime.datetime.now()

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

class RecipeProcedure(db.Model):
    """
    Recipe Procedure Model Data.

    An individual step in a recipe.

    Attributes:
        recipe_id: recipe this belongs to
        recipe_step (int): order of the step in the recipe
        procedure (str): the actual step's text
    """
    __tablename__ = "recipe_procedure"
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    recipe_step = db.Column(db.Integer, nullable=False)
    procedure = db.Column(db.String(100), nullable=False)

    def __init__(self, recipe, step, procedure):
        self.recipe_id = recipe
        self.recipe_step = step
        self.procedure = procedure

class Tag(db.Model):
    """
    Tag Model Data

    Tags used for sorting/filtering recipes.

    Attributes:
        name (str): name of tag
    """
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

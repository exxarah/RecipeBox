""" Data Models for User Functionality """
import datetime
from flask_login import UserMixin
from recipebox import db
from flask_login import current_user
from flask import current_app


class User(UserMixin, db.Model):
    """
    User Model Data. Store user information
    """
    __tablename__ =  "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    recipes = db.relationship('Recipe', backref="user_object", lazy=True)
    likes = db.relationship('Like', backref="user_object", lazy=True)
    ratings = db.relationship('Rating', backref="user_object", lazy=True)
    bio = db.Column(db.String(1024), nullable=True)

    def __init__(self, email, username, password, admin=False):
        self.email = email
        self.username = username
        self.password = password
        self.registered_on = datetime.datetime.now()
        self.admin = admin


class Like(db.Model):
    """
    Like Model Data. An inbetween class for storing recipe likes

    Attributes:
        recipe (Recipe): one to many relationship with recipes
        user (User): one to many relationship with users
    """
    __tablename__ = "like"
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, recipe_id, user_id):
        self.recipe_id = recipe_id
        self.user_id = user_id


class Rating(db.Model):
    """
    Rating Model Data. Inbetween class for recipe ratings

    Attributes:
        recipe (Recipe): one to many relationship with recipes
        user (User): one to many relationship with users
        score (int): int from 1-5 inclusive
    """
    __tablename__ = "rating"
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

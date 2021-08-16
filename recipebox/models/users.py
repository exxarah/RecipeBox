""" Data Models for User Functionality """

from flask import current_app
import os
from recipebox import db

class User(db.Model):
    """
    User Model Data. Store user information
    """
    __tablename__ =  "user"
    id = db.Column(db.Integer, primary_key=True)
    recipes = db.relationship('Recipe', backref="user_object", lazy=True)
    likes = db.relationship('Like', backref="user_object", lazy=True)
    ratings = db.relationship('Rating', backref="user_object", lazy=True)

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

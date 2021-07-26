"""Configuration for RecipeBox"""
import os

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Application Directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
APP_DIR = os.path.join(BASE_DIR, "recipebox")
STATIC_DIR = os.path.join(APP_DIR, "static")

# Define Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(APP_DIR, 'recipebox.db')
SQLALCHEMY_BINDS = {}
DATABASE_CONNECT_OPTIONS = {}

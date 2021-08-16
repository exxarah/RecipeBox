""" MAIN FILE """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Database Setup
db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'recipebox.sqlite')
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_object('config')
    else:
        # Load the test_config if passed if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        pass

    with app.app_context():
        # Database Setup

        from recipebox.models.recipes import Ingredient, Recipe, RecipeIngredient

        db.init_app(app)
        db.create_all()

        from recipebox.recipes import recipe_bp
        from recipebox.general import general_bp

        # Blueprints Setup
        app.register_blueprint(recipe_bp, url_prefix='/')
        app.register_blueprint(general_bp, url_prefix='/')

        return app


app = create_app()

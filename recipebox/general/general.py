from flask import render_template, url_for, request, redirect
from . import general_bp
from ..models.recipes import Ingredient


@general_bp.route('/')
def index():
    # TODO: Add search functions
    return render_template(
        'index.html',
        courses=["Breakfast", "Lunch", "Dinner"],
        ingredients=Ingredient.query.all()
    )

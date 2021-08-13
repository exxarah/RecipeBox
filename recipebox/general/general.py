from flask import render_template, url_for, request, redirect
from . import general_bp


@general_bp.route('/')
def index():
    return render_template('index.html')

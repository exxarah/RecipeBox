""" MAIN FILE """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# APP SETUP
app = Flask(__name__)
app.config.from_object('config')

# DATABASE SETUP
db = SQLAlchemy(app)

import recipebox.models

db.create_all()
db.session.commit()
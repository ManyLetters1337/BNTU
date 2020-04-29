"""
Create App
"""
import os
from flask import Flask
from database.core import db


def create_app(db_url, register_blueprint):
    app = Flask(__name__)
    app.debug = True

    app.secret_key = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url

    db.init_app(app)

    if register_blueprint:
        register_blueprints(app)

    return app


def register_blueprints(app):
    pass
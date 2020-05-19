"""
Create App
"""
import os
from flask import Flask
from database.core import db
from flask_login import LoginManager


login_manager = LoginManager()


def create_app(db_url, register_blueprint):
    app = Flask(__name__)
    app.debug = True

    app.secret_key = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url

    db.init_app(app)

    login_manager.init_app(app)

    if register_blueprint:
        register_blueprints(app)

    return app


def register_blueprints(app):
    from views.categories.categories import categories
    from views.users.auth import auth
    from views.products.products import products
    from views.api.categories.categories import api_categories
    from views.api.orders.orders import api_orders
    from views.api.products.products import api_products

    app.register_blueprint(categories, url_prefix='/categories')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(products, url_prefix='/products')
    app.register_blueprint(api_categories, url_prefix='/api/categories')
    app.register_blueprint(api_orders, url_prefix='/api/orders')
    app.register_blueprint(api_products, url_prefix='/api/products')

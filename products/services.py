"""
Database interaction methods for a Products class
"""
from database.core import db
from database.base_services import BaseDBService
from .models import Products
from flask import session
from sqlalchemy import func
import uuid


class ProductsDBService(BaseDBService):
    model = Products

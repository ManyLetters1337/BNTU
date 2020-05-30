"""
Api For Categories
"""
from flask import Blueprint, jsonify, session, request, url_for
from typing import TYPE_CHECKING
from config import page_size
from database.service_registry import services
from products.models import Products

api_categories = Blueprint('api_categories', __name__)


if TYPE_CHECKING:
    from typing import List
    from categories.models import Categories


@api_categories.route('/', methods=['GET'])
def categories_list():
    """
    Get Categories list
    :return:
    """
    categories: List = services.categories.get_all()

    return jsonify([category.serialize() for category in categories])


@api_categories.route('/<uuid>', methods=['GET'])
def products_in_category(uuid: str):
    """
    Get Products With Specific Category
    :param uuid: UUID for specific category
    :return:
    """
    category: 'Categories' = services.categories.get_by_uuid(uuid)

    products: 'Products' = services.products.get_product_with_category(category)

    return jsonify([product.serialize() for product in products])


@api_categories.route('/active_categories', methods=['GET'])
def get_active_categories():
    """
    Get Active Categories
    :return:
    """
    categories: 'List' = services.categories.get_categories_with_products()

    categories_list = [category.serialize() for category in categories]

    for category in categories_list:
        category['url'] = url_for('categories.category_page', uuid=category['uuid'])

    return jsonify(categories_list)

"""
Api For Products
"""
from flask import Blueprint, jsonify, session, request
from typing import TYPE_CHECKING

from comments.models import Comments
from database.service_registry import services
from orders.models import Orders

api_products = Blueprint('api_products', __name__)


if TYPE_CHECKING:
    from typing import List, Dict
    from categories.models import Categories
    from products.models import Products


@api_products.route('/', methods=['GET'])
def products_list() -> 'Dict':
    """
    Get Products list
    :return:
    """
    products: 'List' = services.products.get_all()

    return jsonify([product.serialize() for product in products])


@api_products.route('/product=<uuid>', methods=['GET'])
def products_info(uuid: str):
    """
    Get Information About Specific Product
    :param uuid: UUID for specific product
    :return:
    """
    product: 'Products' = services.products.get_by_uuid(uuid)

    return jsonify(product.serialize())


@api_products.route('/product=<uuid>/users', methods=['GET'])
def product_users_info(uuid: str):
    """
    Get Information about users for specific product
    :param uuid: UUID for specific product
    :return:
    """
    product: 'Products' = services.products.get_by_uuid(uuid)

    users: 'List' = services.users.get_users_for_product(product)

    return jsonify([user.serialize() for user in users])


@api_products.route('/product=<uuid>/orders', methods=['GET'])
def product_orders_info(uuid: str):
    """
    Get Information about orders for specific Product
    :param uuid: UUID for specific product
    :return:
    """
    product: 'Products' = services.products.get_by_uuid(uuid)

    orders: 'List' = services.orders.get_orders_for_product(product)

    return jsonify([order.serialize() for order in orders])


@api_products.route('/product=<uuid>/tags', methods=['GET'])
def product_tags_info(uuid: str):
    """
    Get Information about tags for specific Products
    :param uuid: UUID for specific products
    :return:
    """
    product: 'Products' = services.products.get_by_uuid(uuid)

    tags: 'List' = services.tags.get_tags_for_product(product)

    return jsonify([tag.serialize() for tag in tags])


@api_products.route('/product=<uuid>/comments', methods=['GET'])
def product_comments_info(uuid: str):
    """
    Get Information about tags for specific Products
    :param uuid: UUID for specific products
    :return:
    """
    product: 'Products' = services.products.get_by_uuid(uuid)

    comments: 'Comments' = services.comments.get_for_product(product)

    return jsonify([comment.serialize() for comment in comments])

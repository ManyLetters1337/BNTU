"""
Api For Users
"""
from flask import Blueprint, jsonify, session, request
from typing import TYPE_CHECKING
from database.service_registry import services
from users.models import Users

api_users = Blueprint('api_users', __name__)


if TYPE_CHECKING:
    from typing import List, Dict


@api_users.route('/', methods=['GET'])
def users_list() -> 'Dict':
    """
    Get Users list
    :return:
    """
    users: 'List' = services.users.get_all()

    return jsonify([user.serialize() for user in users])


@api_users.route('/<uuid>', methods=['GET'])
def user_info(uuid: str):
    """
    Get Information About Specific User
    :param uuid: UUID for specific user
    :return:
    """
    user: 'Users' = services.users.get_by_uuid(uuid)

    return jsonify(user.serialize())


@api_users.route('/<uuid>/orders', methods=['GET'])
def user_orders_info(uuid: str):
    """
    Get Information About User Order
    :param uuid: UUID for specific user
    :return:
    """
    user: 'Users' = services.users.get_by_uuid(uuid)

    orders: 'List' = services.orders.get_orders_for_user(user)

    return jsonify([order.serialize() for order in orders])


@api_users.route('/<uuid>/products', methods=['GET'])
def user_products_info(uuid: str):
    """
    Get Information About User Products
    :param uuid: UUID for specific user
    :return:
    """
    user: 'Users' = services.users.get_by_uuid(uuid)

    products: 'List' = services.products.get_products_for_user(user)

    return jsonify([product.serialize() for product in products])

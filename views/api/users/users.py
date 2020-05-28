"""
Api For Users
"""
from flask import Blueprint, jsonify, session, request
from typing import TYPE_CHECKING

from flask_login import login_required

from comments.models import Comments
from database.service_registry import services
from users.models import Users

api_users = Blueprint('api_users', __name__)


if TYPE_CHECKING:
    from typing import List, Dict


@api_users.route('/', methods=['GET'])
@login_required
def users_list() -> 'Dict':
    """
    Get Users list
    :return:
    """
    users: 'List' = services.users.get_all()

    return jsonify([user.serialize() for user in users])


@api_users.route('/user=<uuid>', methods=['GET'])
@login_required
def user_info(uuid: str):
    """
    Get Information About Specific User
    :param uuid: UUID for specific user
    :return:
    """
    user: 'Users' = services.users.get_by_uuid(uuid)

    return jsonify(user.serialize())


@api_users.route('/user=<uuid>/orders', methods=['GET'])
@login_required
def user_orders_info(uuid: str):
    """
    Get Information About User Order
    :param uuid: UUID for specific user
    :return:
    """
    user: 'Users' = services.users.get_by_uuid(uuid)

    orders: 'List' = services.orders.get_orders_for_user(user)

    return jsonify([order.serialize() for order in orders])


@api_users.route('/user=<uuid>/products', methods=['GET'])
@login_required
def user_products_info(uuid: str):
    """
    Get Information About User Products
    :param uuid: UUID for specific user
    :return:
    """
    user: 'Users' = services.users.get_by_uuid(uuid)

    products: 'List' = services.products.get_products_for_user(user)

    return jsonify([product.serialize() for product in products])


@api_users.route('/comments_statistic=<uuid>/', methods=['GET'])
@login_required
def user_comments_info(uuid: str):
    """
    Get User Comments Info
    :param uuid:
    :return:
    """
    user: 'Users' = services.users.get_by_uuid(uuid)

    comments: 'List' = services.comments.get_for_user(user)

    return jsonify([comment.serialize() for comment in comments])


@api_users.route('/purchased_products=<uuid>', methods=['GET'])
@login_required
def user_purchased_products(uuid: str):
    """
    Get All purchased products for User
    :param uuid:
    :return:
    """
    user: 'Users' = services.users.get_by_uuid(uuid)

    orders: 'List' = services.orders.get_orders_for_user(user)

    products: 'List' = services.products.get_purchased_products_for_user(orders)

    return jsonify([product.serialize() for product in products])

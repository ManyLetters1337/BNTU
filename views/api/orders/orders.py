"""
Api For Orders
"""
from flask import Blueprint, jsonify, session, request
from typing import TYPE_CHECKING
from database.service_registry import services
from orders.models import Orders

api_orders = Blueprint('api_orders', __name__)


if TYPE_CHECKING:
    from typing import List


@api_orders.route('/', methods=['GET'])
def orders_list():
    """
    Get Orders list
    :return:
    """
    orders: List = services.orders.get_all()

    return jsonify([order.serialize() for order in orders])


@api_orders.route('/<uuid>', methods=['GET'])
def order_info(uuid: str):
    """
    Get Information About Specific Order
    :param uuid: UUID for specific order
    :return:
    """
    order: 'Orders' = services.orders.get_by_uuid(uuid)

    return jsonify(order)

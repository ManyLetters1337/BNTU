"""
Api For Orders
"""
from flask import Blueprint, jsonify, session, request
from typing import TYPE_CHECKING

from flask_login import login_required

from database.service_registry import services
from orders.models import Orders
from products.models import Products

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


@api_orders.route('/order=<uuid>', methods=['GET'])
def order_info(uuid: str):
    """
    Get Information About Specific Order
    :param uuid: UUID for specific order
    :return:
    """
    order: 'Orders' = services.orders.get_by_uuid(uuid)

    return jsonify(order.serialize())


@api_orders.route('/product=<uuid>', methods=['GET'])
def orders_for_product(uuid: str):
    """
    Get Orders For Product
    :param uuid:
    :return:
    """
    product: 'Products' = services.products.get_by_uuid(uuid)

    orders: 'List' = services.orders.get_orders_for_product(product)

    return jsonify([order.serialize() for order in orders])

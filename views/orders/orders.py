"""
Orders Views
"""
from typing import TYPE_CHECKING
from flask_login import login_required
from flask import url_for, render_template, redirect, Blueprint, session
from database.service_registry import services
from forms.orders import AcceptOrderForm
from orders.models import Orders
from users.models import Users

if TYPE_CHECKING:
    from products.models import Products

orders = Blueprint('orders', __name__, template_folder='templates')


@orders.route('/order', methods=['GET'])
@login_required
def active_order():
    """
    Product Page
    :return:
    """
    user: 'Users' = services.users.get_by_id(session['user_id'])

    is_having_active = services.orders.get_active_order(user)

    if is_having_active:
        order_: 'Orders' = is_having_active
    else:
        order_: 'Orders' = services.orders.create(user)

    products: 'Products' = services.products.get_products_from_order(order_)

    return render_template('order.html', order=order_, products=products)


@orders.route('/order=<uuid>', methods=['GET'])
@login_required
def specific_order(uuid: str):
    """
    Product Page
    :return:
    """
    user: 'Users' = services.users.get_by_id(session['user_id'])

    order_: 'Orders' = services.orders.get_by_uuid(uuid)

    products: 'Products' = services.products.get_products_from_order(order_)

    return render_template('order.html', order=order_, products=products)


@orders.route('/', methods=['GET'])
@login_required
def orders_page():
    """
    Page With All User Orders
    :return:
    """
    user: 'Users' = services.users.get_by_id(session['user_id'])

    orders_: 'Orders' = services.orders.get_orders_for_user(user)

    return render_template('orders.html', orders=orders_)


@orders.route('/order=<uuid>/delete_product=<product_uuid>', methods=['GET'])
@login_required
def delete_product(uuid: str, product_uuid: str):
    """
    Delete product From Order
    :return:
    """
    order_: 'Orders' = services.orders.get_by_uuid(uuid)
    product: 'Products' = services.products.get_by_uuid(product_uuid)

    order_ = services.orders.remove_product(order_, product)

    return redirect(url_for('orders.orders_page', uuid=order_.uuid))


@orders.route('/oder=<uuid>/accept', methods=['GET'])
@login_required
def accept_order(uuid: str):
    """
    Accept User Order page
    :param uuid: Order uuid
    :return:
    """
    form: 'AcceptOrderForm' = AcceptOrderForm()

    order_: 'Orders' = services.orders.get_by_uuid(uuid)

    return render_template('accept_order.html', form=form, order=order_)


@orders.route('/oder=<uuid>/accept', methods=['POST'])
@login_required
def accept_order_post(uuid: str):
    """
    Accept User Order page POST
    :param uuid: Order uuid
    :return:
    """
    form: 'AcceptOrderForm' = AcceptOrderForm()

    order_: 'Orders' = services.orders.get_by_uuid(uuid)

    if form.validate():
        order_ = services.orders.set_order_detail(order_, country=form.country.data, city=form.city.data,
                                                  address=form.address.data, post_index=form.post_index.data)

        # Add Email Send

        return render_template('successfully_order.html')

    return render_template('accept_order.html', form=form, order=order_)

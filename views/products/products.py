"""
Products views
"""
from typing import TYPE_CHECKING
from flask_login import login_required
from flask import url_for, render_template, redirect, Blueprint, session, request

from comments.models import Comments
from config import photos, basic_image_url, page_size
from database.service_registry import services
from forms.comments import CommentForm
from forms.products import AddProductForm
from orders.models import Orders

if TYPE_CHECKING:
    from products.models import Products
    from categories.models import Categories
    from users.models import Users

products = Blueprint('products', __name__, template_folder='templates')


@products.route('/product=<uuid>', methods=['GET'])
@login_required
def product(uuid: str):
    """
    Product Page
    :return:
    """
    user: 'Users' = services.users.get_by_id(session['user_id'])
    product_: 'Products' = services.products.get_by_uuid(uuid)
    order: 'Orders' = services.orders.get_active_order(user)

    if not order:
        order: 'Orders' = services.orders.create(user)

    is_added = services.orders.product_is_added(order, product_)

    comment_form: 'CommentForm' = CommentForm()

    return render_template('product.html', product=product_, is_added=is_added, comment_form=comment_form)


@products.route('/product=<uuid>', methods=['POST'])
@login_required
def product_post(uuid: str):
    """
    Product Page POST
    :return:
    """
    user: 'Users' = services.users.get_by_id(session['user_id'])
    product_: 'Products' = services.products.get_by_uuid(uuid)
    order_: 'Orders' = services.orders.get_active_order(user)

    is_added = services.orders.product_is_added(order_, product_)

    comment_form: 'CommentForm' = CommentForm()

    if request.form.get('button') == 'Buy':
        is_added = services.users.add_product_to_order(user, product_, order_)

    elif comment_form.validate() and request.form.get('submit') == 'Write':
        comment: 'Comments' = services.comments.create(user, product_, comment_form.text.data)
        comment_form.text.data = ''

        return redirect(url_for('products.product', uuid=product_.uuid))

    return render_template('product.html', product=product_, is_added=is_added, comment_form=comment_form)


@products.route('/', methods=['GET'])
@login_required
def products_list():
    """
    Page with All Products
    :return:
    """
    page: int = int(request.args.get('page', default=1))
    products_ = services.products.get_all()

    return render_template('products.html', products=services.products.apply_pagination(products_, page, page_size))


@products.route('/add_product', methods=['GET'])
@login_required
def add_product():
    """
    Add Product Page
    :return:
    """
    form: AddProductForm = AddProductForm()

    all_categories = services.categories.get_all()
    form.categories.choices = [(category.id, category.name) for category in all_categories]

    return render_template('add_product.html', form=form)


@products.route('/add_product', methods=['POST'])
@login_required
def add_product_post():
    """
    Post Method for Add Product Page
    :return:
    """
    form: 'AddProductForm' = AddProductForm()

    all_categories = services.categories.get_all()
    form.categories.choices = [(category.id, category.name) for category in all_categories]

    if form.validate():

        if form.image.data:
            image_name = photos.save(form.image.data)
            image_url = photos.url(image_name)
        else:
            image_url = basic_image_url

        category: 'Categories' = services.categories.get_by_id(form.categories.data)

        product_: 'Products' = services.products.create(category, name=form.name.data, price=form.price.data,
                                                        description=form.description.data, image=image_url)

        return redirect(url_for('products.product', uuid=product_.uuid))

    return render_template('add_product.html', form=form)

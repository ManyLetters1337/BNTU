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
from forms.products import AddProductForm, create_change_form
from orders.models import Orders

if TYPE_CHECKING:
    from products.models import Products
    from categories.models import Categories
    from users.models import Users

products = Blueprint('products', __name__, template_folder='templates')


@products.route('/product=<uuid>', methods=['GET'])
def product(uuid: str):
    """
    Product Page
    :return:
    """
    product_: 'Products' = services.products.get_by_uuid(uuid)

    is_added = False
    comment_form = None

    if session.get('user_id'):
        user: 'Users' = services.users.get_by_id(session['user_id'])
        order: 'Orders' = services.orders.get_active_order(user)
        comment_form: 'CommentForm' = CommentForm()

        if not order:
            order: 'Orders' = services.orders.create(user)

        is_added = services.orders.product_is_added(order, product_)

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

    elif request.form.get('submit') == 'Написать комментарий' and comment_form.validate():
        comment: 'Comments' = services.comments.create(user, product_, comment_form.text.data)
        comment_form.text.data = ''
        return redirect(url_for('products.product', uuid=product_.uuid))

    elif request.form.get('button') == 'Change':
        return redirect(url_for('products.change_product', uuid=product_.uuid))

    return render_template('product.html', product=product_, is_added=is_added, comment_form=comment_form)


@products.route('product=<uuid>/change', methods=['GET'])
@login_required
def change_product(uuid: str):
    """
    Change Product Data Page
    :param uuid: Product UUID
    :return:
    """
    product_: 'Products' = services.products.get_by_uuid(uuid)

    form: 'AddProductForm' = create_change_form(product_)

    return render_template('change_product.html', form=form)


@products.route('product=<uuid>/change', methods=['POST'])
@login_required
def change_product_post(uuid: str):
    """
    Change Product Data Page
    :param uuid: Product UUID
    :return:
    """
    product_: 'Products' = services.products.get_by_uuid(uuid)

    form: 'AddProductForm' = create_change_form(product_)

    if form.validate():
        if form.image.data:
            image_name = photos.save(form.image.data)
            image_url = photos.url(image_name)
        else:
            image_url = product_.image

        product_: 'Products' = services.products.update(product_, price=request.form.get('price'),
                                                        image=image_url,
                                                        name=request.form.get('name'),
                                                        description=request.form.get('description'),
                                                        category_id=request.form.get('categories'))

        return redirect(url_for('products.product', uuid=product_.uuid))

    return render_template('change_product.html', form=form)


@products.route('/', methods=['GET'])
def products_list():
    """
    Page with All Products
    :return:
    """
    page: int = int(request.args.get('page', default=1))
    products_ = services.products.get_all()

    return render_template('products.html', products=services.products.apply_pagination(products_, page, page_size))


@products.route('/', methods=['POST'])
def products_list_post():
    """
    Page with All Products
    :return:
    """
    page: int = int(request.args.get('page', default=1))
    products_ = services.products.get_all()

    if request.form.get('Search'):
        search_products = services.products.search(request.form.get('Search'))
        return render_template('search_result.html', products=search_products)

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

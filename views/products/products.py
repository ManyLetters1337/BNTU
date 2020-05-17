"""
Products views
"""
from typing import TYPE_CHECKING
from flask_login import login_required
from flask import request, url_for, render_template, redirect, Blueprint, flash
from database.service_registry import services
from forms.products.forms import AddProductForm

if TYPE_CHECKING:
    from products.models import Products
    from categories.models import Categories

products = Blueprint('products', __name__, template_folder='templates')


@login_required
@products.route('/product=<uuid>', methods=['GET'])
def product(uuid: str):
    """
    Product Page
    :return:
    """
    product_: 'Products' = services.products.get_by_uuid(uuid)

    return render_template('product.html', product=product_)


@login_required
@products.route('/', methods=['GET'])
def products_list():
    """
    Page with All Products
    :return:
    """
    products_ = services.products.get_all()

    return render_template('products.html', products=products_)


@login_required
@products.route('/add_product', methods=['GET'])
def add_product():
    """
    Add Product Page
    :return:
    """
    form: AddProductForm = AddProductForm()

    all_categories = services.categories.get_all()
    form.categories.choices = [(category.id, category.name) for category in all_categories]

    return render_template('add_product.html', form=form)


@login_required
@products.route('/add_product', methods=['POST'])
def add_product_post():
    """
    Post Method for Add Product Page
    :return:
    """
    form: 'AddProductForm' = AddProductForm()

    all_categories = services.categories.get_all()
    form.categories.choices = [(category.id, category.name) for category in all_categories]

    if form.validate():
        category: 'Categories' = services.categories.get_by_id(form.categories.data)
        product_: 'Products' = services.products.create(category, name=form.name.data,
                                                        price=form.price.data, description=form.description.data)

        return redirect(url_for('products.product', uuid=product_.uuid))

    return render_template('add_product.html', form=form)

"""
Views for Categories Class
"""
# from config import page_size
from typing import Dict

from flask import url_for, render_template, redirect, session, request, Blueprint

from categories.models import Categories
from config import page_size
from database.service_registry import services
from flask_login import login_required

from forms.categories import AddCategoryForm
from products.models import Products

categories = Blueprint('categories', __name__, template_folder='templates')


@categories.route('/category=<uuid>', methods=['GET'])
@login_required
def category_page(uuid: str):
    """
    Category Page
    :param uuid:
    :return:
    """
    page: int = int(request.args.get('page', default=1))
    category: 'Categories' = services.categories.get_by_uuid(uuid)

    products: 'Products' = services.products.get_products_for_category(category)

    return render_template('category.html', category=category, products=services.products.apply_pagination(products, page, page_size))


@categories.route('/', methods=['GET'])
@login_required
def categories_page():
    """
    Add Category Page
    :return:
    """
    form: 'AddCategoryForm' = AddCategoryForm()

    products_stat = services.products.get_product_categories_statistic()
    categories_: 'Dict' = services.categories.get_categories_statistic(products_stat)

    return render_template('categories.html', form=form, categories=categories_)


@categories.route('/', methods=['POST'])
@login_required
def categories_page_post():
    """
    Add Category Post
    :return:
    """
    form: 'AddCategoryForm' = AddCategoryForm()

    products_stat = services.products.get_product_categories_statistic()
    categories_: 'Dict' = services.categories.get_categories_statistic(products_stat)

    if form.validate():
        category: 'Categories' = services.categories.create(form.name.data)

        return redirect(url_for('categories.categories_page'))
    return render_template('categories.html', form=form, categories=categories_)
"""
Views for Note Class
"""
# from config import page_size
from flask import url_for, render_template, redirect, session, request, Blueprint

from categories.models import Categories
from database.service_registry import services
from flask_login import login_required

from forms.categories import AddCategoryForm

categories = Blueprint('categories', __name__, template_folder='templates')


@categories.route('/', methods=['GET'])
@login_required
def categories_page():
    """
    Page with categories
    :return: Page with categories
    """
    return render_template(
        "/categories.html",
        categories=services.categories.get_all()
    )


@categories.route('/add_category', methods=['GET'])
@login_required
def add_category():
    """
    Add Category Page
    :return:
    """
    form: 'AddCategoryForm' = AddCategoryForm()

    return render_template('add_category.html', form=form)


@categories.route('/add_category', methods=['POST'])
@login_required
def add_category_post():
    """
    Add Category Post
    :return:
    """
    form: 'AddCategoryForm' = AddCategoryForm()

    if form.validate():
        category: 'Categories' = services.categories.create(form.name.data)

        return redirect('categories.categories_page')
    return render_template('add_category.html', form=form)
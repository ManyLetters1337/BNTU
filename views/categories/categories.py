"""
Views for Note Class
"""
# from config import page_size
from flask import url_for, render_template, redirect, session, request, Blueprint
from database.service_registry import services
from flask_login import login_required

categories = Blueprint('categories', __name__, template_folder='templates')


@categories.route('/', methods=['GET'])
# @login_required
def categories_page():
    """
    Page with categories
    :return: Page with categories
    """
    categories_ = services.categories.get_all()

    return render_template(
        "/categories.html",
        categories=categories_
    )
"""
Users Views
"""
from typing import TYPE_CHECKING
from flask_login import login_required
from flask import url_for, render_template, redirect, Blueprint, session, request

from database.service_registry import services

if TYPE_CHECKING:
    from products.models import Products
    from categories.models import Categories
    from users.models import Users

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/user=<id_>', methods=['GET'])
@login_required
def user_page(id_: int):
    """
    Product Page
    :return:
    """
    user: 'Users' = services.users.get_by_id(session['user_id'])

    return render_template('user.html', user=user)

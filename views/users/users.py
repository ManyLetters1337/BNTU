"""
Users Views
"""
from typing import TYPE_CHECKING
from flask_login import login_required
from flask import url_for, render_template, redirect, Blueprint, session, request

from config import photos
from database.service_registry import services
from forms.users import AddInfoForm
from groups.models import Groups

if TYPE_CHECKING:
    from products.models import Products
    from categories.models import Categories
    from users.models import Users

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/user=<id_>', methods=['GET'])
@login_required
def user_page(id_: int):
    """
    User Page
    :return:
    """
    user: 'Users' = services.users.get_by_id(session['user_id'])
    group: 'Groups' = services.groups.get_by_id(user.group_id)

    return render_template('user.html', user=user, group=group)


@users.route('/user=<uuid>/add_info', methods=['GET'])
@login_required
def user_add_info_page(uuid: str):
    """
    User Add Info Page
    :return:
    """
    user: 'Users' = services.users.get_by_id(session['user_id'])

    form: 'AddInfoForm' = AddInfoForm()

    return render_template('add_info.html', user=user, form=form)


@users.route('/user=<uuid>/add_info', methods=['POST'])
@login_required
def user_add_info_page_post(uuid: str):
    """
    Add User Info
    :return:
    """
    user: 'Users' = services.users.get_by_id(session['user_id'])

    form: 'AddInfoForm' = AddInfoForm()
    if form.validate():
        if form.image.data:
            image_name = photos.save(form.image.data)
            image_url = photos.url(image_name)

        user: 'Users' = services.users.update_info(user, image_url, form.about.data, form.birthday_date.data)

        return redirect(url_for('users.user_page', id_=session['user_id']))

    return render_template('add_info.html', user=user, form=form)

"""
Views for Groups Class
"""
# from config import page_size
from typing import Dict, List

from flask import url_for, render_template, redirect, session, request, Blueprint

from database.service_registry import services
from flask_login import login_required
from forms.groups import AddGroupForm
from groups.models import Groups

groups = Blueprint('groups', __name__, template_folder='templates')


@groups.route('/', methods=['GET'])
@login_required
def groups_page():
    """
    Groups Page
    :return:
    """
    form: 'AddGroupForm' = AddGroupForm()

    groups_: 'List' = services.groups.get_all()

    return render_template('groups.html', form=form, groups=groups_)


@groups.route('/', methods=['POST'])
@login_required
def groups_page_post():
    """
    Add Group
    :return:
    """
    form: 'AddGroupForm' = AddGroupForm()

    groups_: 'List' = services.groups.get_all()

    if form.validate():
        group: 'Groups' = services.groups.create(form.number.data)

        return redirect(url_for('groups.groups_page'))
    return render_template('groups.html', form=form, groups=groups_)

"""
Authentication for User Model
"""
from typing import TYPE_CHECKING

from click import BOOL
from flask_login import login_user, login_required, logout_user
from flask import request, url_for, render_template, redirect, Blueprint, flash, session

from celery_tasks import send_reset_password_email
from config import photos, basic_image_url
from create_app import login_manager
from database.service_registry import services
from forms.users import LoginForm, RegistrationForm, ResetPasswordForm, ResetPasswordRequestForm

# from celery_tasks import send_mail, send_reset_password_email
from orders.models import Orders

if TYPE_CHECKING:
    from users.models import Users

login_manager.login_view = 'auth.login'

auth = Blueprint('auth', __name__, template_folder='templates/auth')


@login_manager.user_loader
def load_user(user_id: int) -> 'Users':
    """
    Load current logged-in user
    :param user_id: int (User.id)
    :return: User instance
    """
    return services.users.get_by_id(user_id)


@auth.route('/login', methods=['GET'])
def login():
    """
    User Log In Page
    :return:
    """
    form: LoginForm = LoginForm()

    return render_template('login.html', form=form)


@auth.route('/login', methods=['POST'])
def login_post():
    """
    Post method for User Log In Page
    :return:
    """
    form: LoginForm = LoginForm()

    if form.validate():
        login_user_with_permissions(services.users.get_by_id(services.users.get_by_student_number(
            form.student_number.data).id), form.remember.data)
        return redirect(request.args.get('next') or url_for('products.products_list'))
    return render_template('login.html', form=form)


def login_user_with_permissions(user: 'Users', remember_: 'BOOL'):
    """
    Add User Permissions to Session
    :return:
    """
    session['role'] = user.role
    login_user(user, remember=remember_)


@auth.route('/registration', methods=['GET'])
def registration():
    """
    User Registration Page
    :return:
    """
    form: RegistrationForm = RegistrationForm()

    groups = services.groups.get_all()
    form.group.choices = [(group.id, group.number) for group in groups]

    return render_template('registration.html', form=form)


@auth.route('/registration', methods=['POST'])
def registration_post():
    """
    Post method for User Registration Page
    :return:
    """
    form: RegistrationForm = RegistrationForm()

    groups = services.groups.get_all()
    form.group.choices = [(group.id, group.number) for group in groups]

    if form.validate():
        user: 'Users' = services.users.create(services.groups.get_by_id(form.group.data),
                                              first_name=form.first_name.data,
                                              last_name=form.last_name.data, email=form.email.data,
                                              student_number=form.student_number.data, password=form.password.data,
                                              image=basic_image_url)

        order_: 'Orders' = services.orders.create(user)
        # send_mail.apply_async(args=[form.email.data])
        return redirect(request.args.get('next') or url_for('products.products_list'))
    return render_template('registration.html', form=form)


@auth.route('/reset_password_request', methods=['GET'])
def send_reset_password_token():
    """
    Page where User can change Password
    :return:
    """
    form: ResetPasswordRequestForm = ResetPasswordRequestForm()

    return render_template('send_request_for_reset_password.html', form=form)


@auth.route('/reset_password_request', methods=['POST'])
def send_reset_password_token_post():
    """
    Post method for User reset Password Page
    :return:
    """
    form: ResetPasswordRequestForm = ResetPasswordRequestForm()
    if form.validate():
        user: 'Users' = services.users.get_by_email(form.email.data)
        token = user.get_reset_password_token()
        url = url_for('auth.reset_password', token=token, _external=True)
        send_reset_password_email.apply_async(args=[user.serialize(), url])

        flash("Check your email for the instructions to reset your password")

        return redirect(url_for('auth.login'))
    return render_template('send_request_for_reset_password.html', form=form)


@auth.route('/reset_password/<token>', methods=['GET'])
def reset_password(token):
    """
    Reset user password
    :param token: Token for confirming user
    :return:
    """
    form: ResetPasswordForm = ResetPasswordForm()

    return render_template('reset_password.html', form=form)


@auth.route('/reset_password/<token>', methods=['POST'])
def reset_password_post(token):
    """
    Reset user password Post
    :param token: Token for confirming user
    :return:
    """
    form: ResetPasswordForm = ResetPasswordForm()
    if form.validate():
        user: 'Users' = services.users.verify_reset_password_token(token)
        user = services.users.reset_password(user, form.password.data)
        return redirect(url_for('auth.login'))

    return render_template('reset_password.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    """
    User log out
    :return: Page with Log In form
    """
    logout_user()

    return redirect(url_for('auth.login'))

"""
Authentication for User Model
"""
from typing import TYPE_CHECKING
from flask_login import login_user, login_required, logout_user
from flask import request, url_for, render_template, redirect, Blueprint, flash
from create_app import login_manager
from database.service_registry import services
from forms.users.forms import LoginForm, RegistrationForm, ResetPasswordForm, ResetPasswordRequestForm
# from celery_tasks import send_mail, send_reset_password_email


if TYPE_CHECKING:
    from users.models import User

login_manager.login_view = 'auth.login'

auth = Blueprint('auth', __name__, template_folder='templates/auth')


@login_manager.user_loader
def load_user(user_id: int) -> 'User':
    """
    Load current logged-in user
    :param user_id: int (User.id)
    :return: User instance
    """
    return services.user.get_by_id(user_id)


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
        login_user(services.user.get_by_id(services.user.get_by_student_number(form.student_number.data).id),
                   remember=form.remember.data)
        return redirect(request.args.get('next') or url_for('product.main_page'))
    return render_template('login.html', form=form)


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
    if form.validate():
        user: User = services.user.create(first_name=form.first_name.data, last_name=form.last_name.data,
                                          email=form.email.data, student_number=form.student_number.data,
                                          group_number=form.group_number.data, birthday_date=form.birthday_date.data,
                                          password=form.password.data)
        # send_mail.apply_async(args=[form.email.data])
        return redirect(request.args.get('next') or url_for('product.main_page'))
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
        user: 'User' = services.user.get_by_email(form.email.data)
        token = user.get_reset_password_token()
        url = url_for('auth.reset_password', token=token, _external=True)
        # send_reset_password_email.apply_async(args=[user.email, user.first_name, url])

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
        user: User = services.user.verify_reset_password_token(token)
        user = services.user.reset_password(user, form.password.data)
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
    flash("You have been logged out.")

    return redirect(url_for('auth.login'))
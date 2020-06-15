"""
Forms for User
"""
import datetime
from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField, PasswordField, DateField, SelectField, TextAreaField
from werkzeug.security import check_password_hash
from wtforms.validators import DataRequired, Email, ValidationError, length, EqualTo

from config import photos
from database.service_registry import services
from forms.validators import only_letters, only_numbers


def validate_student_number(form, student_number_field):
    """
    Check Student Number in Forms
    :param form: Form Data
    :param student_number_field: Field with Student number from form (str)
    """
    if not services.users.get_by_student_number(student_number_field.data):
        message = "A user with this student number does not exist"
        flash(message)
        raise ValidationError(message)


def validate_user_password(form, password_field):
    """
    Check user password
    :param form: Form Data
    :param password_field: Field with User password from Form (str)
    """
    if services.users.get_by_student_number(form.student_number.data):
        if not check_password_hash(services.users.get_password_hash(services.users.get_uuid_by_student_number(
                form.student_number.data)), password_field.data):
            message = "Wrong Password"
            flash(message)
            raise ValidationError(message)


class LoginForm(FlaskForm):
    """
    Login Form for User
    """
    student_number = StringField("Студенческий номер", validators=[DataRequired(), validate_student_number, only_numbers, length(4, 100)])
    password = PasswordField("Пароль", validators=[DataRequired(), validate_user_password, length(6, 30)])
    remember = BooleanField("Запомнить меня")
    submit = SubmitField('Войти')


def check_user_in_db(form, student_number_field):
    """
    Checking the presence of a user in the database
    :param form: Form Data
    :param student_number_field: Field with Student Number from Form
    """
    if services.users.get_by_student_number(student_number_field.data):
        message = "User already exist"
        flash(message)
        raise ValidationError(message)


def validate_passwords(form, password_field):
    """
    Check passwords are the same
    :param form: Form Data
    :param password_field: Field with Password from Form
    """
    if not form.password_repeat.data == password_field.data:
        message = "Passwords do not match"
        flash(message)
        raise ValidationError(message)


def validate_date(form, date_field):
    """
    Validate Data Field
    :param form: Form Data
    :param date_field: Field with Data from Form
    """
    if date_field.data > datetime.date.today():
        message = "Date should be normal"  # Change text
        flash(message)
        raise ValidationError(message)


def validate_password_content(form, password_field):
    """
    Checking for a capital letter in a string
    :param form: Form Data
    :param password_field: Field with Password from Form
    """
    upper_letter = False
    for i in password_field.data:
        if i.isupper:
            upper_letter = True
    if not upper_letter:
        message = "The password must contain a capital letter"
        flash(message)
        raise ValidationError(message)


def check_email_in_db(form, field):
    """
    Check user with this email in database
    :param form:
    :param field:
    :return:
    """
    if services.users.get_by_email(field.data):
        message = "User with this email already exist"
        flash(message)
        raise ValidationError(message)


class RegistrationForm(FlaskForm):
    """
    Registration Form for User
    """
    first_name = StringField("Имя", validators=[DataRequired(), only_letters, length(2, 100)])
    last_name = StringField("Фамилия", validators=[DataRequired(), only_letters, length(2, 100)])
    email = StringField("Email", validators=[DataRequired(), Email(), length(4, 100), check_email_in_db])
    group = SelectField("Номер Группы", coerce=int)
    student_number = StringField("Номер студентческого", validators=[DataRequired(), check_user_in_db, only_numbers, length(4, 100)])
    password = PasswordField("Пароль", validators=[DataRequired(), validate_password_content, length(6, 30)])
    password_repeat = PasswordField("Повторите пароль", validators=[DataRequired(), EqualTo('password'), length(6, 30)])
    submit = SubmitField("Зарегистрироваться")


class AddInfoForm(FlaskForm):
    """
    Add Additional Info For User
    """
    birthday_date = DateField("Дата рождения", validators=[DataRequired()])
    about = TextAreaField("О себе", validators=[DataRequired()])
    image = FileField("Изображение", validators=[DataRequired(), FileAllowed(photos, 'Только изображение!')])
    submit = SubmitField("Подтвердить")


def validate_user_existing(form, email_field):
    """
    Check user existing
    :param form: Form Data
    :param email_field: Email Field from Form
    :return:
    """
    if not services.users.get_by_email(email_field.data):
        message = "User with this email dose not exist"
        flash(message)
        raise ValidationError(message)


class ResetPasswordRequestForm(FlaskForm):
    """
    Form for Send Request to Reset User Password
    """
    email = StringField("Email", validators=[DataRequired(), Email(), length(6, 100), validate_user_existing])
    submit = SubmitField()


class ResetPasswordForm(FlaskForm):
    """
    Form for Reset Password
    """
    password = PasswordField("Password", validators=[DataRequired(), validate_password_content, length(6, 30)])
    password_repeat = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo('password'), length(6, 30)])
    submit = SubmitField()

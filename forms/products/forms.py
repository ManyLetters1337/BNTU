"""
Forms for Products
"""
import datetime
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, DecimalField
from werkzeug.security import check_password_hash
from wtforms.validators import DataRequired, Email, ValidationError, length, EqualTo
from database.service_registry import services
from ..validators import only_letters, only_numbers


class AddProductForm(FlaskForm):
    """
    Login Form for User
    """
    name = StringField("Name", validators=[DataRequired(), length(4, 100)])
    image = StringField("Image", validators=[])
    categories = SelectField("Category", validators=[DataRequired()], coerce=int)
    price = DecimalField("Price", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired(), length(4, 100)])
    submit = SubmitField()


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

"""
Forms for Products
"""
import datetime
from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, SubmitField, BooleanField, SelectField, DecimalField, FileField
from wtforms.validators import DataRequired, Email, ValidationError, length, EqualTo
from database.service_registry import services
from forms.validators import only_letters, only_numbers
from config import photos
from products.models import Products


def create_change_form(product: 'Products') -> 'AddProductForm':
    """
    Create Change Product Form
    :return:
    """
    form: 'AddProductForm' = AddProductForm()

    all_categories = services.categories.get_all()

    form.categories.choices = [(category.id, category.name) for category in all_categories]
    form.categories.data = product.category_id
    form.name.data = product.name
    form.description.data = product.description
    form.price.data = product.price

    return form


class AddProductForm(FlaskForm):
    """
    Add Product Form
    """
    name = StringField("Название", validators=[DataRequired(), length(4, 100)])
    categories = SelectField("Категория", validators=[DataRequired()], coerce=int)
    price = DecimalField("Цена", validators=[DataRequired()])
    description = StringField("Описание", validators=[DataRequired(), length(4, 100)])
    image = FileField("Изображение", validators=[FileAllowed(photos, 'Только изображение!')])
    submit = SubmitField('Добавить')


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

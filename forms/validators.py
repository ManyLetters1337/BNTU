"""
Base validators
"""
from flask import flash
from wtforms.validators import ValidationError


def only_letters(form, field):
    """
    Checking that the field contains only letters
    :param form: Form Data
    :param field: Field from Form
    """
    if not field.data.isalpha():
        message = "Field must contain only letters"
        flash(message)
        raise ValidationError(message)


def only_numbers(form, field):
    """
    Checking that the string contains only numbers
    :param form: Form Data
    :param field: Field from Form
    """
    if not field.data.isdigit():
        message = "Поле должно содержать только цифры"
        flash(message)
        raise ValidationError(message)

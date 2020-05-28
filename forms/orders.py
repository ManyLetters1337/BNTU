"""
Forms for Orders
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, DecimalField, FileField
from wtforms.validators import DataRequired, Email, ValidationError, length, EqualTo
from database.service_registry import services
from forms.validators import only_letters, only_numbers


class AcceptOrderForm(FlaskForm):
    """
    Accept Order Form
    """
    country = StringField("Страна", validators=[DataRequired(), length(2, 100)])
    city = StringField("Город", validators=[DataRequired(), length(2, 100)])
    address = StringField("Адрес", validators=[DataRequired(), length(4, 100)])
    post_index = StringField("Почтовый индекс", validators=[DataRequired(), length(2, 20), only_numbers])
    submit = SubmitField()

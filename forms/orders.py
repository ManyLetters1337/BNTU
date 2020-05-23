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
    country = StringField("Country", validators=[DataRequired(), length(2, 100), only_letters])
    city = StringField("City", validators=[DataRequired(), length(2, 100), only_letters])
    address = StringField("Address", validators=[DataRequired(), length(4, 100)])
    post_index = StringField("Post Index", validators=[DataRequired(), length(2, 20), only_numbers])
    submit = SubmitField()

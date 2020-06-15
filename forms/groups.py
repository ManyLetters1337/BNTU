"""
Forms for Groups
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length
from forms.validators import only_numbers


class AddGroupForm(FlaskForm):
    """
    Add Group Form
    """
    number = StringField("Номер группы", validators=[DataRequired(), length(2, 100), only_numbers])
    submit = SubmitField('Добавить Группу')

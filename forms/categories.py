"""
Forms for Categories
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length


class AddCategoryForm(FlaskForm):
    """
    Add Category Form
    """
    name = StringField("Название", validators=[DataRequired(), length(2, 100)])
    submit = SubmitField('Добавить категорию')

"""
Forms for Comments
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, DecimalField, FileField, TextAreaField
from wtforms.validators import DataRequired, length


class CommentForm(FlaskForm):
    """
    Accept Order Form
    """
    text = TextAreaField("Комментарий", validators=[DataRequired(), length(2, 300)])
    submit = SubmitField()

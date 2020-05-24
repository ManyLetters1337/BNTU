"""
Forms for Comments
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, DecimalField, FileField
from wtforms.validators import DataRequired, length


class CommentForm(FlaskForm):
    """
    Accept Order Form
    """
    text = StringField("Comment", validators=[DataRequired(), length(2, 100)])
    submit = SubmitField()

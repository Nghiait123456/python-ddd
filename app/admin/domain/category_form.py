from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CategoryForm(FlaskForm):
    name = StringField(
        '카테고리명',
        validators=[DataRequired(), Length(min=2, max=25)]
    )

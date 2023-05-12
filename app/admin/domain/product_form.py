from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class ProductForm(FlaskForm):
    name = StringField(
        '제품명',
        validators=[DataRequired(), Length(min=2, max=25)]
    )
    price = IntegerField(
        '가격',
        validators=[DataRequired(), NumberRange(min=0)]
    )
    detail = StringField('설명')

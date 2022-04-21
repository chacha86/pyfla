from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

class ArticleForm(FlaskForm) :
    title = StringField('제목', validators=[DataRequired()])
    body = TextAreaField('내용', validators=[DataRequired()])
    member_id = HiddenField('작성자', validators=[DataRequired()])
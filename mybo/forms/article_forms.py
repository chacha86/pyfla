from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, PasswordField
from wtforms.validators import DataRequired, InputRequired, EqualTo

class ArticleForm(FlaskForm) :
    title = StringField('제목', validators=[DataRequired()])
    body = TextAreaField('내용', validators=[DataRequired()])
    member_id = HiddenField('작성자', validators=[DataRequired()])
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, InputRequired, EqualTo

class MemberForm(FlaskForm) :
    login_id = StringField('아이디', validators=[DataRequired('아이디를 입력해주세요.')])
    login_pw = PasswordField('비밀번호', validators=[InputRequired('비밀번호를 입력해주세요'), EqualTo('login_pw2', message='비밀번호가 일치하지 않습니다')])
    login_pw2 = PasswordField('비밀번호2')
    nick_name = StringField('별명', validators=[DataRequired('실명을 입력해주세요.')])
    real_name = StringField('실명', validators=[DataRequired('별명을 입력해주세요.')])

class LoginForm(FlaskForm):
    login_id = StringField('아이디', validators=[InputRequired()])
    login_pw = TextAreaField('비밀번호', validators=[InputRequired()])

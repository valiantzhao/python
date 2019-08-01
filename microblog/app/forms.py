from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(message=u"用户名不能为空")])
    password = PasswordField('Password', validators=[DataRequired(message=u"密码不能为空"), Length(
        10, 20, message=u'长度位于10~20之间')], render_kw={'placeholder': u'输入密码'})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

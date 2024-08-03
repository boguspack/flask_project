from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, EqualTo
class loginform(FlaskForm):
    username=StringField("userame",validators=[DataRequired(),length(min=3,max=20)])
    password=PasswordField("password",validators=[DataRequired()])
    submit=SubmitField("login")
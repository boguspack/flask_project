from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError
from models import User

class signupform(FlaskForm):
    firstname=StringField("First Name",validators=[DataRequired(),length(min=3,max=20)])
    lastname=StringField("Last Name",validators=[DataRequired(),length(min=3,max=10)])
    email=StringField("Email Address",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    confirmpassword=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo("password")])
    gender=SelectField("gender", choices=[  ('male', 'Male'),('female', 'Female')],validators=[DataRequired()])
    DOB=DateField("Date of Birth", format='%Y-%m-%d',validators=[DataRequired()])
    submit=SubmitField("Sign Up")

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("email already taken mf")

class loginform(FlaskForm):
    email=StringField("Email Address",validators=[DataRequired()])
    password=PasswordField("password",validators=[DataRequired()])
    submit=SubmitField("login")


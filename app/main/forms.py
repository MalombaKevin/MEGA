from turtle import title
from typing import Optional
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo, Optional
from ..models import User, Megapitch
from wtforms import ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter your username',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Sign Up')
def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class addMegaPitch(FlaskForm):
    theme = SelectField('Choose Theme Project',choices=[('Science', 'Science'),('Engineering', 'Engineering')],validators= [Optional()] )
    title = StringField('Enter project title',validators = [DataRequired()])
    contributors = StringField('Enter project contributors',validators = [DataRequired()])
    pitch = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Pitch it')

    
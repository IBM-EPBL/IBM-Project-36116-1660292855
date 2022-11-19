from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from plasma.models import User


class RegistrationForm(FlaskForm):
    name = StringField('Full Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('User Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email ID',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Security Key', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Security Key',
                                     validators=[DataRequired(), EqualTo('password')])
    contact_no = StringField('Mobile',
                           validators=[DataRequired(), Length(min=2, max=20)])
    gender = RadioField('Gender', choices=['Male', 'Female'])
    role = RadioField('Role', choices=['Donar', 'Pateients'])
    blood_group = StringField('Blood Type', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email ID',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Security Key', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class SearchForm(FlaskForm):
    blood_group = StringField('Search Plasma Donor - Blood Group',
                        validators=[DataRequired()])
    submit = SubmitField('Find')

class MessageForm(FlaskForm):
    to_id = StringField('Enter Email ID', validators=[DataRequired()])
    message = StringField('Text', validators=[DataRequired()])
    submit = SubmitField('Send')
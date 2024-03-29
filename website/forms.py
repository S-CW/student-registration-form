from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import InputRequired, Email, Length

from models import Course, Session, Student

class Login(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    student_name = StringField('name', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

    def validate_email(self, email):
        if Student.query.filter_by(email=email.data).first():
            raise ValidationError("Email already registered!")

    def validate_username(self, username):
        if Student.query.filter_by(username=username.data).first():
            raise ValidationError("Username already taken! Please try a different username.")


def choice_query_option():
    return Course.query

def choice_query_datetime():
    return Session.query

class ChoiceForm(FlaskForm):
    option = QuerySelectField(query_factory=choice_query_option, allow_blank=True, get_label='subject')
    timeslot = QuerySelectField(query_factory=choice_query_datetime, allow_blank=True, get_label='datetime')

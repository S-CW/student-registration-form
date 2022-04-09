from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

from models import Student, Course, Session
from extension import db, login_manager
import forms


bp = Blueprint('auth', __name__)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(user_id)

import app

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.Login()

    if form.validate_on_submit():
        user = Student.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)

                # redirect user to user view
                return '<h1>you are logged in</h1>'
        
        return '<h1>Invalid username or password</h1>'


    return render_template('login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'




@bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = forms.RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Student(username=form.username.data, student_name=form.student_name.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'

    return render_template('signup.html', form=form)


@bp.route('/test')
def testing():
    return '<h1>Ok</h1>'

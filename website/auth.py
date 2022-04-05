from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user




bp = Blueprint('auth', __name__)

import app

@bp.route('/')
def index():
    return "<p>Home Page</p>"


@bp.route('/login', methods=['GET', 'POST'])
def login():
    pass


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))




@bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    pass


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mydev:password@localhost/course_table'
    db.init_app(app)

    from .models import registered_student, Student, Course, Session

    app.route('/')
    def index():
        return "<p>Home Page</p>" 

    app.route('/login')
    def login():
        return "<p>Login Page</p>" 

    app.route('/user/<username>')
    def profile():
        return "<p>User</p>"


    return app




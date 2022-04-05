from flask_login import UserMixin
from extension import db


# Table for many to many relationship of student table and course table
registered_student = db.Table('registered_student', 
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(150))
    subject_interested = db.relationship('Course', secondary=registered_student, lazy='subquery', backref=db.backref('registered', lazy=True))

    
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80), nullable=False)
    sessions = db.relationship('Session', backref='course', lazy=True)

# One to many relation of course table to session table
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False)
    classroom = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)




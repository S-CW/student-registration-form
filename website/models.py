from flask_login import UserMixin
from extension import db


# Table for many to many relationship of student table and course table
class Enrolled(db.Model):
    __tablename__ = "student_enrolled"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id =  db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)

    __table_args__ = (db.UniqueConstraint(student_id, course_id, session_id),)

    student = db.relationship('Student', backref='student_course_session', passive_deletes='all')
    course = db.relationship('Course', backref='student_course_session', passive_deletes='all')
    session = db.relationship('Session', backref='student_course_session', passive_deletes='all')


class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    student_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80))
    courses = db.relationship('Course', secondary='student_enrolled')

    
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(80), nullable=False)
    credit_score = db.Column(db.Integer, nullable=False, default=0)
    code = db.Column(db.Integer, nullable=False, default=0)
    student = db.relationship('Student', secondary='student_enrolled')
    
    def __repr__(self):
        return 'Choice {}'.format(self.subject)

# One to many relation of course table to session table
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(50), nullable=False)
    classroom = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))




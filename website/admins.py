
from flask import redirect, url_for, flash
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_admin import AdminIndexView

from extension import admin, db, login_manager
from models import Student, Course, Enrolled, Session

@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(user_id)

# Model
class StudentModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash('You are not logged in. Log in to view')
        return redirect(url_for('auth.login'))

    column_list = [
        'username',
        'student_name',
        'email'
    ]

    column_searchable_list = [
        'username',
        'student_name',
        'email'
    ]

    column_editable_list = [
        'email'
    ]

    column_filters = [
        'username',
        'student_name',
        'email'
    ]

class CourseModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash('You are not logged in. Log in to view')
        return redirect(url_for('auth.login'))


class RegModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash('You are not logged in. Log in to view')
        return redirect(url_for('auth.login'))

    column_list = [
        'student.student_name',
        'student.email',
        'course.subject',
        'session.datetime',
        'session.classroom'
    ]

    column_labels = {
        'student.student_name' : 'Name',
        'student.email' : 'Email',
        'course.subject' : 'Subject',
        'session.datetime' : 'Datetime',
        'session.classroom' : 'Classroom'
    }


# # Admin home page
class MyAdminHomeView(AdminIndexView):
    def is_accessible(self):
        return True
    
    
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        flash('You are not logged in. Log in to view')
        return redirect(url_for('auth.login'))

    

admin.add_view(StudentModelView(Student, db.session))
admin.add_views(CourseModelView(Course, db.session))
admin.add_view(RegModelView(Enrolled, db.session))

from flask import redirect, url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_admin import AdminIndexView

from extension import admin, db, login_manager
from models import Student, Course, Session

@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(user_id)

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login'))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login'))

admin.add_view(MyModelView(Course, db.session))
admin.add_view(MyModelView(Student, db.session))
admin.add_view(MyModelView(Session, db.session))

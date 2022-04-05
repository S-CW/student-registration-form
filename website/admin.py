from flask_admin.contrib.sqla import ModelView

from extension import admin, db
from models import Student, Course, Session

admin.add_view(ModelView(Course, db.session))
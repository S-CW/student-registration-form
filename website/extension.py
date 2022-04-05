from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate



db = SQLAlchemy()
admin = Admin()
login = LoginManager()
migrate = Migrate()
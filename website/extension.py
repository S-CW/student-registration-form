from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate

from flask_bootstrap import Bootstrap


Bootstrap = Bootstrap()
db = SQLAlchemy()
admin = Admin()
migrate = Migrate()
login_manager = LoginManager()

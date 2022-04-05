from multiprocessing import Manager
from flask import Flask
import admin
from extension import db, admin, login, migrate
from auth import bp
import models



def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    
    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(bp)
    
    return app
    
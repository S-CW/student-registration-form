from flask import Flask

import admins
from extension import db, admin, login_manager, migrate, Bootstrap
from auth import bp
from views import bp2



def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    
    db.init_app(app)
    admin.init_app(app, index_view=admins.MyAdminHomeView())
    migrate.init_app(app, db)
    login_manager.init_app(app)
    Bootstrap.init_app(app)

    app.register_blueprint(bp)
    app.register_blueprint(bp2)
    
    return app
    
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import config



db = SQLAlchemy()
migrate = Migrate()

def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    # initialized the database
    db.init_app(app)
    migrate.init_app(app, db)


    from .routes.home import home_route
    from .routes.admin import admin_route
    from .routes.meetings import meetings_route
    from .routes.login import login_route
    from .routes.users import users_route

    app.register_blueprint(home_route)
    app.register_blueprint(users_route, url_prefix='/users')
    app.register_blueprint(admin_route, url_prefix='/admin')
    app.register_blueprint(meetings_route, url_prefix='/meetings')
    app.register_blueprint(login_route, url_prefix='/login')

    return app
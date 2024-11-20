import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import config
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

#from flask_tinymce import TinyMCE

db = SQLAlchemy()
migrate = Migrate()
flask_bcrypt = Bcrypt()
login_manager = LoginManager()
#tinymce = TinyMCE()


def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    
    # initialized the database
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
 #   tinymce.init_app(app)
 
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRETE_KEY') #'your_strong_secret_key'
    app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY') #'your_jwt_secret_key'
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    
 



    from .routes.home import home_route
    from .routes.admin import admin_route
    from .routes.meetings import meetings_route
    from .routes.login import login_route
    from .routes.users import users_route
    from .routes.register import register_route


    app.register_blueprint(home_route)
    app.register_blueprint(users_route, url_prefix='/users')
    app.register_blueprint(admin_route, url_prefix='/admin')
    app.register_blueprint(meetings_route, url_prefix='/meetings')
    app.register_blueprint(login_route, url_prefix='/login')
    app.register_blueprint(register_route, url_prefix='/register')

    return app
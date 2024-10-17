import os
from flask import Flask, render_template, request, redirect, url_for, render_template
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt 

#app = Flask(__name__)

#Configuration
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
#db.init_app(app)

# database
#db = SQLAlchemy()
#migrate = Migrate()

# from config.py 
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# initialize app 
#db.init_app(app)
# migrate
#migrate.init_app(app, db)


# Cria o aplicativo com as configurações 
from . import create_app # from __init__ file

app = create_app(os.getenv("CONFIG_MODE"))


# JWT 
jwt = JWTManager(app)


# inicializa
if __name__ == '__main__':
    app.run(debug=True)


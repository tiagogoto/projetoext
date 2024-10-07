import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt 
from routes.home import home_route
from routes.admin import admin_route
from routes.meetings import meetings_route
from routes.login import login_route


app = Flask(__name__)

#Configuration


# database
db = SQLAlchemy()

jwt = JWTManager(app)

app.register_blueprint(home_route)

app.register_blueprint(admin_route, url_prefix='/admin')

app.register_blueprint(meetings_route, url_prefix='/meetings')
app.register_blueprint(login_route, url_prefix='/login')

if __name__ == '__main__':
    app.run(debug=True)


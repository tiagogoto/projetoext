from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
home_route = Blueprint('home', __name__)

@home_route.route('/')

def home():
    name = current_user
    if name.is_authenticated == False:
        titulo = "Sistema de Gestão de reuniões"
        return render_template('login.html', titulo=titulo)
    else:
        return redirect(url_for('users.user_detail'))

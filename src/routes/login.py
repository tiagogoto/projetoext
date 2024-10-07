from flask import Blueprint, render_template

login_route = Blueprint('login', __name__)

@login_route.route('/')
def login():
    titulo = "Sistema de Gestão de reuniões"
    return render_template('login.html', titulo=titulo)
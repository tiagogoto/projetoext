from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/')

def home():
    titulo = "Sistema de Gestão de reuniões"
    return render_template('index.html', titulo=titulo)

from flask import Blueprint, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from ..models.entities.users import Users
from ..models.repository.users_repository import Users_repository, Reg_permission
from dotenv import load_dotenv
from os import getenv

load_dotenv(".env.admin")

admin_route = Blueprint('admin', __name__)

@admin_route.route('/')
@login_required
def lista_configadmin():
   
    user = Users.query.filter_by(userid=current_user.userid).first()
    print(f"usuário: {user.username}")
    if user.access != 1:
        return render_template("no_permission.html")
    titulo = "Administração do Sistema"
    return render_template('admin_panel.html', titulo=titulo)


@admin_route.route('/token', methods=['GET'])
@login_required
def check_token():
    
    frase = f'identificação: {current_user}'
    return frase


@admin_route.route('/create_admin', methods=['GET'])
def create_admin():
    users = Users_repository.get_list()
    print(users)
    exist = False
    dados = {'username':"administrador",
            'userpassword':getenv('USER_PASSWORD'),
            'userid':'admin',
            'useremail':getenv('ADMIN_EMAIL'),
            'userpermission':1,
            'is_active': True
         }
    for user in users:
        if user:
            exist = True
            return "Já existe um administrador"

    if not exist:
        Reg_permission.insert("Administrador")
        Users_repository.insert_user(dados=dados)
    
    return redirect(url_for('login.login_form'))


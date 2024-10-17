from flask import Blueprint, render_template
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from ..models.entities.users import Users
admin_route = Blueprint('admin', __name__)

@admin_route.route('/')
@login_required
def lista_configadmin():
   
    user = Users.query.filter_by(userid=current_user.userid).first()
    print(f"usuário: {user.username}")
    if user.access != 0:
        return "Erro Você não tem permissão esta aqui!"
    titulo = "Administração do Sistema"
    return render_template('admin_panel.html', titulo=titulo)


@admin_route.route('/token', methods=['GET'])

def check_token():
    
    frase = f'identificação: {current_user}'
    return frase


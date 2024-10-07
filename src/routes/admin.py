from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required
admin_route = Blueprint('admin', __name__)

@admin_route.route('/')
#@jwt_required()
def lista_configadmin():
    #user_id = get_jwt_identity()
    #user = user.query.filter_by(id=user_id).first()
    titulo = "Administração do Sistema"
    return render_template('index.html', titulo=titulo)

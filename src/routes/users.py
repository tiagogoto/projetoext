from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.repository.users_repository import Users_repository, Reg_permission
from ..models.entities.users import Users
from .. import db
from flask_login import login_required, current_user

users_route = Blueprint('users', __name__)

@users_route.route('/')
@login_required
def list_users():
    users_list = Users_repository.get_list()
    return render_template('list_users.html', dados = users_list)

@users_route.route('/insertform')
def register_form():
    return render_template('user_form.html')

@users_route.route('/', methods=['POST'])
def register_users():
    if request.method == "POST":
        username  = request.form.get('username')
        userpassword =  request.form.get('userpassword')
        userid = request.form.get('userid')
        useremail = request.form.get('useremail')
        userpermission = request.form.get('userpermission')
        active = request.form.get('is_active')
        if active == "true":
            active_bool =  True
        else:
            active_bool = False
        dados= {'username': username,
            'userpassword':userpassword,
            'userid':userid,
            'useremail':useremail,
            'userpermission':userpermission,
            'is_active': active_bool
              }
        usuario = Users()
        usuario.insert_user(dados)
    else:
        return "Erro, no envio de dados"
   
    return  redirect(url_for('users.list_users'))

@users_route.route('/<int:id>',methods=['GET'] )
def update_user(id):
    if request.method == "GET":
        user = Users.query.get(id)
        return f"ID obtido: {user.username}"
    return redirect(url_for('users.list_users'))
# {'username': username, 'userpassword':userpassword}

    
@users_route.route('/detail', methods=['GET'])
@login_required
def user_detail():
    name= current_user
    return render_template('user_detail.html', dados=name)
    
@users_route.route('/permission', methods=['GET'])
@login_required
def gets_permission():
    permission_list = Reg_permission.gets()
    return render_template('user_permission.html', data = permission_list)

@users_route.route('/permission', methods=['POST'])
@login_required
def insert_permission():
    name = request.form.get('name')
    Reg_permission.insert(name)
    flash("Nova permissão cadastrado com sucesso")
    return redirect(url_for('users.gets_permission'))

@users_route.route('/permission_del/<id>', methods=['POST'])
@login_required
def del_permission(id):
    Reg_permission.delete(id)
    flash("Grupo de permissão deletado")
    return redirect(url_for('users.gets_permission'))


"""
@meetings_route.route('/', methods=['POST'])
def insert_meetings():
    pass

@meetings_route.route('/<int:clientes_id>')
def consult_meeting(meeting_id):
    pass

@meetings_route.route('/<int:clientes_id>/edit', methods=['PUT'])
def edit_meeting(meeting_id):
    pass

@meetings_route.route('/<int:clientes_id>/delete', methods=['DELETE'])
def delete_meeting(meeting_id):
    pass
    
"""
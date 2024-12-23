from flask import request, jsonify
from ..entities.users import Users, Permission

from ... import flask_bcrypt
from .. import db

class Users_repository():
    def get_list():
        user_list = db.session.execute(db.select(Users).order_by(Users.id)).scalars()
        return user_list
    def get_admin():
        admin = db.session(db.select(Users).where(Users.userid == "admin")).first()
    def insert_user( dados):
        user = Users(username = dados['username'],
                     _password = flask_bcrypt.generate_password_hash(dados['userpassword']).decode('utf-8'),
                     userid = dados['userid'],
                     useremail = dados['useremail'],
                     access = dados['userpermission'],
                     isactive = dados['is_active']
                     )
        db.session.add(user)
        db.session.commit()
    
class Reg_permission():
    def gets():
        permi_list = db.session.execute(db.select(Permission).order_by(Permission.id)).scalars()
        return permi_list
    def insert(descri):
        permission = Permission(description = descri)
        db.session.add(permission)
        db.session.commit()
    
    def delete(id):
        permission =db.one_or_404(db.select(Permission).filter_by(id=id))
        db.session.delete(permission)
        db.session.commit()
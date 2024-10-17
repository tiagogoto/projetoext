from flask import request, jsonify
from ..entities.users import Users, Permission
import uuid
from ... import db


class Users_repository():
    def get_list():
        user_list = db.session.execute(db.select(Users).order_by(Users.id)).scalars()
        return user_list
    
    def insert_user(self, dados):
        user = Users(username = dados['username'],
                     userpassword = dados['userpassword'],
                     userid = dados['userid'],
                     useremail = dados['useremail'],
                     access = dados['userpermission'],
                     is_active = dados['is_active']
                     )
        db.session.add(user)
        db.session.commit()

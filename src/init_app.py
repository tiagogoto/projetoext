#!/usr/bin/env python
from dotenv import load_dotenv
from os import getenv
from flask import current_app
from app import app
from . import flask_bcrypt
from .models.entities.users import Users
from .models.repository.users_repository import Users_repository
from . import db

load_dotenv(".env.admin")


def main():
    """Main entry point for script."""
    with app.app_context():
        db.metadata.create_all(db.engine)
        if Users_repository.get_list():
            print('Usuário já existe!!')
            return

        dados = {
            'username':"administrador",
            'userpassword':getenv('USER_PASSWORD'),
            'userid':'admin',
            'useremail':getenv('ADMIN_EMAIL'),
            'userpermission':1,
            'is_active': True
         }
        Users_repository.insert_user(dados)
        # permission configuration
        
        
        print('User added.')
    return


if __name__ == '__main__':
    sys.exit(main())
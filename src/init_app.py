#!/usr/bin/env python
from dotenv import load_dotenv
from os import getenv

from .models.entities.users import Users
from .models.repository.users_repository import Users_repository, Reg_permission
from .models import db




load_dotenv(".env.admin")

def start():
    """Main entry point for script."""
    with app.app_context():
        Reg_permission.insert("Administrador")
        dados = {'username':"administrador",
            'userpassword':getenv('USER_PASSWORD'),
            'userid':'admin',
            'useremail':getenv('ADMIN_EMAIL'),
            'userpermission':1,
            'is_active': True
         }
        Users_repository.insert_user(dados=dados)
        # permission configuration   
        print('User added.')
    return


if __name__ == '__main__':
    sys.exit(start())
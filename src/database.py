import os
from .models.entities.users import Users

def create_admin(db, bcrypt):
    admin = Users(
                username="administrador",
                useremail="admin@g.com",
                _password=bcrypt.generate_password_hash("123456789").decode('utf-8'),
                userid = "admin",
                access=0,
                is_active=True
            )
    db.session.add(admin)
    db.session.commit()
    db.close_all_sessions()



if __name__ == '__main__':
    create_admin()
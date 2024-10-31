import os
#from .models.entities.users import Users
from .models.entities.institution import Country
# from ... import db, flask_bcrypt
import csv
"""
def create_admin(db, flask_bcrypt):
    admin = Users(
                username="administrador",
                useremail="admin@g.com",
                _password=flask_bcrypt.generate_password_hash("123456789").decode('utf-8'),
                userid = "admin",
                access=0,
                is_active=True
            )
    db.session.add(admin)
    db.session.commit()
    db.close_all_sessions()
"""
def create_country(db):
    with open('country.csv', mode='r') as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            newcountry = Country(name = line[1], acronym = line[0])
            db.session.add(newcountry)
            db.session.commit()
    

if __name__ == '__main__':
    #create_admin()
    create_country()
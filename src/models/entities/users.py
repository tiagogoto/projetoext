
from  ... import db
#from flask_validator import ValidateEmail, ValidateString, ValidateCountry
from sqlalchemy.orm import validates


class Users(db.Model):
    __tablename__="users"
    #__table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False)
    userpassword= db.Column(db.Text, nullable=False)
    userid = db.Column(db.Text, nullable=False, unique=True)
    useremail = db.Column(db.Text, nullable=False)
    access = db.Column(db.Integer, db.ForeignKey("permissions.id"))
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Permission(db.Model):
    __tablename__="permissions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<ID: {self.id} - Permission {self.descricao} >'
    


"""
class Meeting_type(Base):
    __tablename__="meeting_type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(Text, nullable=False)
    def __repr__(self):
        return f"Id {id} nome do tipo: {type_name}"

class Subject(Base):
    __tablename__="subject"
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(Tex, nullable=False)
    def __repr__(self):
        return f"Id {id} nome da Pauta: {type_name}"

class Meeting_subject(Base):
    __tablename__=""
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(Tex, nullable=False)
    def __repr__(self):
        return f"Id {id} nome da Pauta: {type_name}"
"""
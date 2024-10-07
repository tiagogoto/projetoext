from sqlalchemy import Integer, Column, Text
from db.db import Base


class Users(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Text, nullable=False)
    userpassword= Column(Text, nullable=False)
    userid = Column(Text, nullable=False)
    useremail = Column(Text, nullable=False)
    access = Column(Text, nullable = False)
    is_active = Column(bool, default=True) 
    def __repr__(self):
        return f'<User {self.username}>'   

class Permission(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    


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
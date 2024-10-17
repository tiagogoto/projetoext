from  ... import db, flask_bcrypt

#from flask_validator import ValidateEmail, ValidateString, ValidateCountry
from sqlalchemy.orm import validates



class Users(db.Model):
    __tablename__="users"
    #__table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text, nullable=False)
    _password= db.Column(db.Text, nullable=False)
    userid = db.Column(db.Text, nullable=False, unique=True)
    useremail = db.Column(db.Text, nullable=False)
    access = db.Column(db.Integer, db.ForeignKey("permissions.id"))
    authenticated = db.Column(db.Boolean, default=False)
    isactive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, value):
          self._password = flask_bcrypt.generate_password_hash(value).decode('utf-8')
          db.session.commit()

    def check_password(self, value):
        return flask_bcrypt.check_password_hash(self._password, value)
    
    def get_list():
        user_list = db.session.execute(db.select(Users).order_by(Users.id)).scalars()
        return user_list
    
    def insert_user(self, dados):
        user = Users(username = dados['username'],
                     _password = flask_bcrypt.generate_password_hash(dados['userpassword']).decode('utf-8'),
                     userid = dados['userid'],
                     useremail = dados['useremail'],
                     access = dados['userpermission'],
                     is_active = dados['is_active']
                     )
        db.session.add(user)
        db.session.commit()    
    def is_active(self):
        """True, as all users are active."""
        return self.isactive

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.userid

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
    

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
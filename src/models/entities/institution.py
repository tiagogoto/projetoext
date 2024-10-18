from  ... import db, flask_bcrypt
from sqlalchemy.orm import validates



class Country(db.Model):
    __tablename__ ='country'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    acronym = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Country {self.name}'

    def register(self, data):
        self.name = data['name']
        self.acronym = data['name']
        db.session.commit()

    def get_list():
        return db.session.execute(db.select(Country).order_by(Country.id)).scalars()

class Institution(db.Model):
    __tablename__='institution'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    acronym = db.Column(db.Text, nullable=False)
    country = db.column(db.Integer, db.ForeignKey("country.id"), nullable=False )
    
    def __repr__(self):
        return f'<Institution {self.name}>'
    
    def register(self, data):
        self.name = data['name']
        self.acronym = data['acronym']
        db.session.commit()

class Department(db.Model):
    __tablename__='department'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    acronym = db.Column(db.Text, nullable=False)
    inst_id = db.Column(db.Integer, db.ForeignKey('institution.id'))

    def __repr__(self):
        return f'< Unidade: {self.name}>'
    
    def register(self, data):
        self.name =  data['name']
        self.acronym = data['acronym']
        self.inst_id = data['inst_id']
        db.session.commit()

class Course(db.Model):
    __tablename__= 'course'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    depart_id = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __repr__(self):
        return f'Course: {self.name}'

    def register(self, data):
        self.name = data['name']
        self.depart_id = data['department']
        db.session.commit()

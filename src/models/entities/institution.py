from  ... import db, flask_bcrypt
from sqlalchemy.orm import validates



class Country(db.Model):
    __tablename__ ='country'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    acronym = db.Column(db.Text, nullable=False)
    institution = db.relationship("Institution", back_populates="country", lazy='dynamic')

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
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False )
    country =  db.relationship("Country", back_populates="institution")
    department = db.relationship("Department", back_populates="institution", lazy='dynamic')

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
    institution = db.relationship("Institution", back_populates="department")
    course = db.relationship("Course", back_populates="department", lazy='dynamic')
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
    department = db.relationship("Department", back_populates="course")
    meeting = db.relationship("Meetings", back_populates="course", lazy='dynamic')
    numbering = db.relationship("Numbering", back_populates="course", lazy='dynamic')
    attendee = db.relationship("Attendees", back_populates="course", lazy='dynamic')
    def __repr__(self):
        return f'Course: {self.name}'

    def register(self, data):
        self.name = data['name']
        self.depart_id = data['department']
        db.session.commit()

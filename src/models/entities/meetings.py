from ... import db
from sqlalchemy.orm import validates

class Meetings(db.Model):
    __tablename__ = "meetings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meet_type = db.Column(db.Integer, db.ForeignKey('meeting_type.id'), nullable=False)
    meet_number = db.Column(db.Integer, nullable=False)
    meet_description = db.Column(db.Text, nullable=False)
    meet_date = db.Column(db.DateTime, default=datetime.utcnow)


class Meeting_type(db.Model):
    __tablename__="meeting_type"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f"Id {id} nome do tipo: {type_name}"

class Subject(Base):
    __tablename__="subject"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_name = db.Column(db.Tex, nullable=False)
    def __repr__(self):
        return f"Id {id} nome da Pauta: {type_name}"

class Meeting_subject(Base):
    __tablename__=""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_name = db.Column(db.Tex, nullable=False)
    def __repr__(self):
        return f"Id {id} nome da Pauta: {type_name}"
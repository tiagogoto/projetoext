from ... import db
from sqlalchemy.orm import validates
from datetime import datetime

class Meetings(db.Model):
    __tablename__ = "meetings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meet_type = db.Column(db.Integer, db.ForeignKey('meeting_type.id'), nullable=False)
    meet_number = db.Column(db.Integer, nullable=False)
    meet_description = db.Column(db.Text, nullable=False)
    meet_regdate = db.Column(db.DateTime, default=datetime.timezone.utc)
    meet_date = db.Column(db.DateTime, nullable = False)
    meet_location = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f"Meeting id: {self.id}, Meet_type: {self.meet_number}"

class Meeting_type(db.Model):
    __tablename__="meeting_type"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f"Id {id} nome do tipo: {self.type_name} "

class Metting_agenda(db.Model):
    __tablename__="meeting_agenda"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agenda_name = db.Column(db.Tex, nullable=False)
    agenda_protocol = db.Column(db.Text, nullable = True)
    agenda_interested = db.Column(db.Text, nullable = True)
    agenda_description = db.Column(db.Text, nullable= True)
    meeting_id = db.Column(db.Integer, db.ForeignKey('meetings.id'), nullable=False)
    def __repr__(self):
        return f"Id {id} nome da Pauta: {type_name}"

"""
class Meeting_agenda(Base):
    __tablename__="meeting_subject"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agenda_status = db.Column(db.Boolean)
    def __repr__(self):
        return f"Id {id} nome da Pauta: {type_name}"
   """
 
class Meeting_minute(db.Model):
    __tablename__='meeting_minute'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    minutes_number = db.Column(db.Integer )
    meeting_id = db.Column(db.Integer, db.ForeignKey('meetings.id'), nullable=False)
    addannotation = db.Column(db.Text, nullable = True)
    aproved_date = db.column(db.DateTime, nullable=False)
    recorded_by = db.Column(db.Text, nullable= False)
    def __repr__(self):
        return f"Id: {id} "


class Meeting_attendees(db.Model):
    __tablename__='meeting_attendees'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meetings_id = db.Column(db.Integer, db.ForeignKey('meetings.id'))
    attendee_name = db.Column(db.Text)
    attendee_id = db.Column(db.Text, nullable=True)

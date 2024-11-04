from ... import db
from sqlalchemy.orm import validates
 
from datetime import datetime

class Meetings(db.Model):
    __tablename__ = "meetings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meet_number = db.Column(db.Integer, nullable=False)
    meet_description = db.Column(db.Text, nullable=False)
    meet_regdate = db.Column(db.DateTime, default=datetime.now)
    meet_date = db.Column(db.DateTime, nullable = False)
    meet_location = db.Column(db.Text, nullable = False)
    ##
    # relationshipMeetings_attendees
    #  meeting type
    meet_type_id = db.Column(db.Integer, db.ForeignKey('meeting_type.id'), nullable=False)
    meet_type = db.relationship("Meeting_type", back_populates="meeting")
    # agenda
    meeting_agenda = db.relationship("Meeting_agenda", back_populates="meeting", lazy='dynamic')
    # meeting minutes
    minutes = db.relationship("Meeting_minute", back_populates="meeting", lazy='dynamic')
    # meeting_attendees
    attendees = db.relationship("Meeting_attendees", back_populates="meeting", lazy='dynamic')
    
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable = False)
    course = db.relationship("Course", back_populates="meeting")
    def __repr__(self):
        return f"Meeting id: {self.id}, Meet_type: {self.meet_number}"

class Meeting_type(db.Model):
    __tablename__="meeting_type"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.Text, nullable=False)
    meeting = db.relationship("Meetings", back_populates="meet_type", lazy='dynamic')
    numbering = db.relationship("Numbering", back_populates="meet_type", lazy="dynamic")
    def __repr__(self):
        return f"Id {id} nome do tipo: {self.type_name}"

class Meeting_agenda(db.Model):
    __tablename__="meeting_agenda"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    agenda_topic = db.Column(db.Text, nullable=False)
    agenda_protocol = db.Column(db.Text, nullable = True)
    agenda_interested = db.Column(db.Text, nullable = True)
    agenda_description = db.Column(db.Text, nullable= True)
    meeting_id = db.Column(db.Integer, db.ForeignKey('meetings.id'), nullable=False)
    meeting = db.relationship("Meetings", back_populates="meeting_agenda")
    
    minute_id = db.Column(db.Integer, db.ForeignKey('meeting_minute.id'), nullable=True)
    minute = db.relationship("Meeting_minute", back_populates="meeting_agenda")

    def __repr__(self):
        return f"Id {id} nome da Pauta: {type_name}"
    
class Meeting_minute(db.Model):
    __tablename__='meeting_minute'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    minute_number = db.Column(db.Integer )
    
    addannotation = db.Column(db.Text, nullable = True)
    aproved_date = db.Column(db.DateTime, nullable = False)
    recorded_by = db.Column(db.Text, nullable= False)
    # foreignKey
    meeting_id = db.Column(db.Integer, db.ForeignKey('meetings.id'), nullable=False)
    meeting = db.relationship("Meetings", back_populates="minutes")
    
    
    # meeting minute
    meeting_agenda = db.relationship("Meeting_agenda", back_populates="minute", lazy='dynamic')
    def __repr__(self):
        return f"Id: {id} "

class Meeting_attendees(db.Model):
    __tablename__='meeting_attendees'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meetings_id = db.Column(db.Integer, db.ForeignKey('meetings.id'))
    meeting = db.relationship("Meetings", back_populates="attendees")
   
    #attendee_name = db.Column(db.Text, nullable=False)
    attendee_id = db.Column(db.Text, db.ForeignKey('attendees.id'), nullable=True)
    attendee = db.relationship('Attendees', back_populates="meeting_attendees")
    def __repr__(self):
        return f"ID {self.id} meeting: {self.meetings_id}"
    

class Attendees(db.Model):
    __tablename__ = 'attendees'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    document = db.Column(db.Text, nullable=True)
    meeting_attendees = db.relationship("Meeting_attendees", back_populates="attendee", lazy='dynamic')
    def __repr__(self) -> str:
        return f"ID: {self.id} name: {self.name}"
    
class Numbering(db.Model):
    __tablename__= 'numering'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer)
    me_type_id = db.Column(db.Integer, db.ForeignKey('meeting_type.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    # relationship
    meet_type = db.relationship('Meeting_type', back_populates='numbering')
    course = db.relationship("Course", back_populates="numbering")

from ... import db
from ..entities.meetings import Meeting_attendees, Meeting_type, Meetings, Meeting_minute, Attendees, Meeting_agenda
 


class Reg_meetings():
    def gets():
        meetings_list = db.session.execute(db.select(Meetings).order_by(Meetings.id)).scalars()
        return meetings_list
    
    def gets_meeting(id):
        meeting = db.session.execute(db.select(Meetings).filter_by(id = id))
        return meeting
    
    def register_meeting(data):
        meeting = Meetings(meeting_number = data["number"],
                           meet_description = data["description"],
                           meet_date = data["date"],
                           meet_location = data["date"],
                           meet_location = data["location"],
                           meet_type_id = data["type"])
        db.session.add(meeting)
        db.session.commit()
    
    def gets_by_course(courseid):
        meetings_list = db.session.execute(db.select(Meetings).order_by(Meetings.meet_date).filter_by(course_id = courseid)).scalars()
        return meetings_list
    
    
class Reg_meeting_type():
    def gets():
        types_list = db.session.execute(db.select(Meeting_type).order_by(Meeting_type.id)).scalars()
        return types_list
    
    def insert(name):
        type = Meeting_type(type_name= name )
        db.session.add(type)
        db.session.commit()

class Reg_attendees():
    def gets():
        atteendees_list = db.session.execute(db.select(Attendees).order_by(Attendees.name)).scalars()
        return atteendees_list
    def insert(aname, adocument):
        attendee = Attendees(name = aname, document = adocument )
        db.session.add(attendee)
        db.session.commit()
    
class Reg_meeting_atten():
    def gets():
        meeting_atte = db.session.execute(db.select(Meeting_attendees).order_by(Meeting_attendees.meetings_id)).scalars()
        return meeting_atte
    
    def insert(id, att_id):
        attendee = Meeting_attendees(meetings_id = id, attendee_id = att_id)
        db.session.add(attendee)
        db.session.commit()
    
class Reg_meet_minutes():
    def gets():
        meeting_miniutees_list = db.session.execute(db.select(Meeting_attendees).order_by(Meeting_minute.id)).scalars()
        return meeting_miniutees_list

    def insert(num, annot, rec, me_id, me_at):
        minute = Meeting_minute(minute_number = num, 
                                addannotation = annot,
                                recorded_by= rec,
                                meeting_id = me_id, 
                                meeting_attendees_id = me_at)
        db.session.add(minute)
        db.session.commit()

class Reg_agenda():
    def gets():
        agenda_list = db.session.execute(db.select(Meeting_agenda).order_by(Meeting_agenda.id)).scalars()
        return agenda_list
    
    def insert(topic, protocol, interested, description, meid,mi_id ):
        agenda = Meeting_agenda(
            agenda_topic = topic,
            agenda_protocol = protocol,
            agenda_interested = interested,
            agenda_description = description,
            meeting_id = meid,
            minute_id =mi_id
        )
        db.session.add(agenda)
        db.session.commit()
    

        
        
        

        
        
        
        


from ... import db
from ..entities.meetings import Meeting_attendees, Meeting_type, Meetings, Meeting_minute, Attendees, Meeting_agenda, Numbering
 


class Reg_meetings():
    def gets():
        meetings_list = db.session.execute(db.select(Meetings).order_by(Meetings.id)).scalars()
        return meetings_list
    
    def get_meeting(id):
        meeting = db.session.execute(db.select(Meetings).filter_by(id = id)).scalar()
        return meeting
    
    def insert_meeting(data):
        meeting = Meetings(meet_number = data["number"],
                           meet_description = data["description"],
                           meet_date = data["date"],
                           meet_location = data["location"],
                           meet_type_id = data["type"],
                           course_id = data["course"])        
        db.session.add(meeting)
        db.session.commit()
        return meeting.id
    
    def gets_by_course(courseid):
        meetings_list = db.session.execute(db.select(Meetings).order_by(Meetings.meet_date).filter_by(course_id = courseid)).scalars()
        return meetings_list
    
    def update_description(meet_id, descrip):
        meeting = db.session.execute(db.select(Meetings).filter_by(id=meet_id)).scalar()
        meeting.meet_description = descrip
        db.session.commit()
    def get_meeting_number(meeting_id):
        meeting = db.session.execute(db.select(Meetings).filter_by(id=meeting_id)).scalar()
        return meeting.meet_number
    
    
class Reg_meeting_type():
    def gets():
        types_list = db.session.execute(db.select(Meeting_type).order_by(Meeting_type.id)).scalars()
        return types_list
    
    def insert(name):
        type = Meeting_type(type_name= name )
        db.session.add(type)
        db.session.commit()

    def delete(id):
        type_s = db.one_or_404(db.select(Meeting_type).filter_by(id=id))
        db.session.delete(type_s)
        db.session.commit()
        

class Reg_attendees():
    def gets():
        atteendees_list = db.session.execute(db.select(Attendees).order_by(Attendees.name)).scalars()
        return atteendees_list
    
    def insert(aname, adocument, course):
        attendee = Attendees(name = aname, document = adocument, course_id = course )
        db.session.add(attendee)
        db.session.commit()

    def delete(id):
        attendee = db.one_or_404(db.select(Attendees).filter_by(id=id))
        db.session.delete(attendee)
        db.session.commit()
    def get_one(id):
        attendee = db.get_or_404(db.select(Attendees).filter_by(id=id))
        return attendee
    

        

class Reg_meeting_atten():
    def gets():
        meeting_atte = db.session.execute(db.select(Meeting_attendees).order_by(Meeting_attendees.meetings_id)).scalars()
        return meeting_atte
    
    def get_list(mee_id):
        list_attendees = db.session.execute(db.select(Meeting_attendees).filter_by(meetings_id=mee_id)).scalars().all()
        return list_attendees
    
    def insert(id, att_id):
        attendee = Meeting_attendees(meetings_id=id, attendee_id = att_id)
        db.session.add(attendee)
        db.session.commit()
    def update_attendance(id, stat):
        attendee = db.session.execute(db.select(Meeting_attendees).filter_by(id=id)).scalar()
        attendee.status = stat
        db.session.commit()
    
class Reg_meet_minutes():
    def gets():
        meeting_miniutees_list = db.session.execute(db.select(Meeting_attendees).order_by(Meeting_minute.id)).scalars()
        return meeting_miniutees_list
    
    def get_minute(meeting_id):
        minute = db.session.execute(db.select(Meeting_minute).filter_by(meeting_id = meeting_id)).scalar()
        return minute

    def insert(num, rec, me_id, end, quo):
        minute = Meeting_minute(minute_number = num, 
                                recorded_by= rec,
                                meeting_id = me_id,
                                endtime = end,
                                quorum = quo 
                                )
        db.session.add(minute)
        db.session.commit()

class Reg_agenda():
    def gets():
        agenda_list = db.session.execute(db.select(Meeting_agenda).order_by(Meeting_agenda.id)).scalars()
        return agenda_list
    def get_meet_agenda(id):
        list_agenda = db.session.execute(db.select(Meeting_agenda).filter_by(meeting_id=id)).scalars()
        return list_agenda
    def insert(topic, protocol, interested, description, meid ):
        agenda = Meeting_agenda(
            agenda_topic = topic,
            agenda_protocol = protocol,
            agenda_interested = interested,
            agenda_description = description,
            meeting_id = meid,
        )
        db.session.add(agenda)
        db.session.commit()
    def update(ag_id, descrip, stat, notes):
        agenda = db.session.execute(db.select(Meeting_agenda).filter_by(id=ag_id)).scalar()
        agenda.status = stat
        agenda.notes = notes
        agenda.agenda_description = descrip
        db.session.commit()

class Reg_numbering():
    def gets_all():
        numbering_list = db.session.execute(db.select(Numbering).order_by(Numbering.id)).scalars()
        return numbering_list
    def insert(courseid, meet_typeid):
        num = db.session.execute(db.select(Numbering).filter_by(course_id = courseid).where(Numbering.me_type_id == meet_typeid)).scalar()
        if num == None:
            numm = Numbering(number=1, me_type_id = meet_typeid, course_id = courseid)
            db.session.add(numm)
            db.session.commit()
            return numm.number
        else:
            num.number += 1
            db.session.commit()

        return num.number
        



    

    

        
        
        

        
        
        
        


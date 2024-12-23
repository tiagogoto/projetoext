from flask import request, jsonify
from ..entities.institution import Country, Institution, Course, Department, Organization
import uuid
from .. import db

class Reg_country():
    def insert_reg(cname,cacronym ):
        country =  Country(name = cname, acronym = cacronym)
        db.session.add(country)
        db.session.commit()
    def update_reg(id, name, acronym):
        country = db.one_or_404(db.select(Country).filter_by(id = id)) 
        # db.session.execute()
        country.name = name
        country.acronym = acronym
        db.session.commit()

    def delete_reg(id):
        country = db.one_or_404(db.select(Country).filter_by(id = id))
        db.session.delete(country)
        db.session.commit()
    def get_countries():
        country_list = db.session.execute(db.select(Country).order_by(Country.id)).scalars()
        return country_list




class Reg_inst():
    def insert_reg(inst_name,inst_acronym, inst_country, logo ):
        institution =  Institution(name = inst_name, acronym = inst_acronym, country_id=inst_country, logo=logo)
        db.session.add(institution)
        db.session.commit()
    def update(id, name, acronym, country, logo):
        institution = db.one_or_404(db.select(Institution).filter_by(id = id)) 
        # db.session.execute()
        institution.name = name
        institution.acronym = acronym
        institution.country_id = country
        institution.logo = logo
        db.session.commit()

    def delete_reg(id):
        institution = db.one_or_404(db.select(Institution).filter_by(id = id))
        db.session.delete(institution)
        db.session.commit()
    
    def get_institutions():
        institutions_list = db.session.execute(db.select(Institution).order_by(Institution.id)).scalars()
        return institutions_list
    
    def get_institutions_join():
        Institution_list = db.session.execute(db.select(Institution).join(Country, Country.id == Institution.country).order_by(Institution.id)).scalars()
        return Institution_list
    def get_one_inst(inst_id):
        institution = db.session.execute(db.select(Institution).filter_by(id=inst_id)).scalar()
        return institution

class Reg_depart():
    def insert_reg(name, acronym, inst):
        department =  Department(name = name, acronym = acronym, inst_id=inst)
        db.session.add(department)
        db.session.commit()
    def update_reg(id, name, acronym, inst):
        department = db.one_or_404(db.select(Department).filter_by(id = id)) 
        # db.session.execute()
        department.name = name
        department.acronym = acronym
        department.inst_id = inst
        db.session.commit()

    def delete_reg(id):
        department = db.one_or_404(db.select(Department).filter_by(id = id))
        db.session.delete(department)
        db.session.commit()
    
    def get_departments():
        department_list = db.session.execute(db.select(Department).order_by(Department.id)).scalars()
        return department_list
    

class Reg_course():
    def insert_reg(name, depart ):
        course =  Course(name = name, depart_id = depart)
        db.session.add(course)
        db.session.commit()

    def update_reg(id, name, depart):
        course = db.one_or_404(db.select(Course).filter_by(id = id)) 
        # db.session.execute()
        course.name = name
        course.depart_id = depart
        db.session.commit()

    def delete_reg(id):
        course = db.one_or_404(db.select(Course).filter_by(id = id))
        db.session.delete(course)
        db.session.commit()
    
    def get_courses():
        course_list = db.session.execute(db.select(Course).order_by(Course.id)).scalars()
        return course_list
    
    def gets_join():
        course_list = db.session.execute(db.select(Course).join(Department).order_by(Course.name)).scalars()
        return course_list


class Reg_organizationI:
    def insert(self, oname, oacronym, ologo):
        org = Organization(name=oname, acronym=oacronym, logo=ologo)
        db.session.add(org)
        db.session.commit()
    def update_logo(self,  ologo):
        org = db.session.execute(db.select(Organization).filter_by(id=1)).scalar()
        org.logo = ologo
        db.coomit()


        
    

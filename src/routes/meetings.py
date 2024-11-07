from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from ..models.repository.meetings import Reg_meetings, Reg_meeting_type, Reg_agenda, Reg_attendees, Reg_meet_minutes, Reg_meeting_atten, Reg_numbering
from ..models.repository.register import Reg_course
from ..routes.home import home_route
from .. import db, login_manager
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
meetings_route = Blueprint('meetings', __name__)


"""
Rotas meetings

    - /meetings/ (GET) - Listar as reuniões
    - /meetings/ (POST) - inserir as reuniões 
    - /meetings/new (GET) - renderizar o formulário para cadastrar reuniões
    - /meetings/<id> (GET) - obter os dados de uma reunião
    - /meeting/<id>/update (PUT)  - atualizar os dados da reunião 

"""

# Meeting

@meetings_route.route('/')
@login_required
def list_meetings():
    meetings_date = Reg_meetings.gets()
    return render_template('list_meetings.html', dados= meetings_date)


@meetings_route.route('/form')
@login_required
def show_meeting_form():
    meet_type_list = Reg_meeting_type.gets()
    courses = Reg_course.gets_join()
    return render_template('meeting_form.html', type_list = meet_type_list, course_list = courses)



@meetings_route.route('/', methods=['POST'])
@login_required
def insert_meetings():
    # data from form
    meet_type = request.form.get('typename')
    list_of_atteendees =  request.form.getlist('field[]')
    list_of_agenda = request.form.getlist('field2[]')
    da = request.form.get('date')
    descrip = request.form.get('description')
    loc = request.form.get('location')
    course = request.form.get('course')
    print(type(meet_type))
    print(type(course))
    #  insert datas
    number =  Reg_numbering.insert(course, meet_type)
    #Reg_meetings.insert_meeting()
    print(number)
    

    return jsonify(list_of_atteendees, list_of_agenda, da, descrip,loc ,course,meet_type, 200)

@meetings_route.route('/<int:clientes_id>')
def consult_meeting(meeting_id):
    pass

@meetings_route.route('/<int:clientes_id>/edit', methods=['PUT'])
def edit_meeting(meeting_id):
    pass

@meetings_route.route('/<int:clientes_id>/delete', methods=['DELETE'])
def delete_meeting(meeting_id):
    pass

## meeting type

@meetings_route.route('/meeting_type', methods=['GET'])
@login_required
def list_meeting_type():
    meeting_type_list = Reg_meeting_type.gets()
    return render_template('meeting_type.html', dados = meeting_type_list)

@meetings_route.route('/meeting_type', methods=['POST'])
@login_required
def insert_meeting_type():
    name_type = request.form.get('name')
    Reg_meeting_type.insert(name_type)
    flash("Salvo com sucesso!!")
    return redirect(url_for('meetings.list_meeting_type'))

@meetings_route.route('/meeting_type_del/<id>', methods=['POST'])
@login_required
def del_meeting_type(id):
    Reg_meeting_type.delete(id)
    flash('Deletado com Sucesso')
    return redirect(url_for('meetings.list_meeting_type'))


## Ateendees 

@meetings_route.route('/ateendees', methods=['GET'])
@login_required
def gets_attendees():
    list_attendees = Reg_attendees.gets()
    return render_template('list_attendees.html', data = list_attendees)

@meetings_route.route('/ateendees', methods=['POST'])
@login_required
def insert_attendees():
    name = request.form.get('name')
    document = request.form.get('document')
    Reg_attendees.insert(name, document)
    flash("Inserido com sucesso!")
    return redirect(url_for('gets_attendees'))


@meetings_route.route('/attendees/<id>/del', methods=['POST'])
@login_required
def del_attendees(id):
    Reg_attendees.delete(id)
    flash("Participantes deletado com sucesso")
    return redirect(url_for('gets_attendees'))

"""@meetings_route.route('/attendees/<id>', methods=['GET'])
def get_one_attendee(id):
   """

######
#  Meeting attendees list
@meetings_route.route('/meet_attendees', methods=['GET'])
def show_attendee():
    lis = Reg_meeting_atten.gets()
    return render_template('attendees_list.html', data=lis)





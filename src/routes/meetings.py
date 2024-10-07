from flask import Blueprint, render_template
from database.meetings import meetings_date
from routes.home import home_route
meetings_route = Blueprint('meetings', __name__)
"""
Rotas meetings

    - /meetings/ (GET) - Listar as reuniões
    - /meetings/ (POST) - inserir as reuniões 
    - /meetings/new (GET) - renderizar o formulário para cadastrar reuniões
    - /meetings/<id> (GET) - obter os dados de uma reunião
    - /meeting/<id>/update (PUT)  - atualizar os dados da reunião 

"""



@meetings_route.route('/')
def list_meetings():
    return render_template('list_meetings.html', dados= meetings_date)

@meetings_route.route('/', methods=['POST'])
def insert_meetings():
    pass

@meetings_route.route('/<int:clientes_id>')
def consult_meeting(meeting_id):
    pass

@meetings_route.route('/<int:clientes_id>/edit', methods=['PUT'])
def edit_meeting(meeting_id):
    pass

@meetings_route.route('/<int:clientes_id>/delete', methods=['DELETE'])
def delete_meeting(meeting_id):
    pass
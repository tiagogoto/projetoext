from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.entities.institution import Country, Course, Department, Institution
from ..models.repository.register import Reg_country, Reg_inst, Reg_course, Reg_depart
from .. import db, login_manager
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

register_route = Blueprint('register', __name__)

@register_route.route('/', methods=['GET'])
@login_required
def register_page():
    return render_template('register_page.html')


# country ------

@register_route.route('/country', methods=['GET'])
@login_required
def country_list_form():
    country_list = Reg_country.get_countries()
    if not country_list:
        country_list = []
    return render_template('reg_country_form.html', country_list = country_list)

# register a new country
@register_route.route('/country', methods=['POST'])
@login_required
def reg_country():
    if request.method == "POST":
        country_name = request.form.get('country_name')
        country_acronym = request.form.get('country_acronym')
        Reg_country.insert_reg(country_name, country_acronym)
        flash('Cadastro realizado com sucesso')
    else:
        return "Erro, no envio de dados"
    
    return redirect(url_for('register.country_list_form'))

# delete a row
@register_route.route('/country/<id>', methods=['POST'])
@login_required
def country_del(id):
    Reg_country.delete_reg(id)
    flash('Operação realizado com sucesso')
    return redirect(url_for('register.country_list_form'))

# update a row
@register_route.route('/country/<id>', methods=['PUT'])
@login_required
def country_update(id):

    return redirect(url_for('register.country_list_form'))

###############
# -- Institutiton
#

# view 
@register_route.route('/institution', methods=['GET'])
@login_required
def inst_list():
    institution_list = Reg_inst.get_institutions_join()#get_institutions()
    print(institution_list)
    country_list = Reg_country.get_countries()

    return render_template('reg_institution.html', country_list = country_list, institution_list=institution_list)
# insert institution
@register_route.route('/institution', methods=['POST'])
@login_required
def reg_inst():
    inst_name = request.form.get('inst_name')
    inst_acronym = request.form.get('inst_acronym')
    inst_country = request.form.get('inst_country')
    Reg_inst.insert_reg(inst_name= inst_name, inst_acronym=inst_acronym, inst_country=inst_country)
    flash('Cadastro Realizado com Sucesso')
    return redirect(url_for('register.inst_list'))

# delete
@register_route.route('/institution/<id>', methods=['POST'])
@login_required
def del_inst(id):
    Reg_inst.delete_reg(id)
    flash('Operação realizado com sucesso')
    return redirect(url_for('register.inst_list'))

##################
# department
# view department
@register_route.route('/department', methods=['GET'])
@login_required
def dep_list():
    department_list = Reg_depart.get_departments()
    inst_list = Reg_inst.get_institutions()
    return render_template('reg_department.html', inst_list = inst_list, department_list=department_list)

# insert department
@register_route.route('/department', methods=['POST'])
@login_required
def reg_dep():
    dep_name = request.form.get('dep_name')
    dep_acronym = request.form.get('dep_acronym')
    dep_inst = request.form.get('dep_inst')
    Reg_depart.insert_reg(dep_name, dep_acronym, dep_inst)
    flash('Cadastro Realizado com Sucesso')
    return redirect(url_for('register.dep_list'))

# delete
@register_route.route('/department/<id>', methods=['POST'])
@login_required
def del_dep(id):
    Reg_depart.delete_reg(id)
    flash('Operação realizado com sucesso')
    return redirect(url_for('register.dep_list'))

##############
#  course

@register_route.route('/course', methods=['GET'])
@login_required
def course_list():
    course_list = Reg_course.get_courses()
    dep_list = Reg_depart.get_departments()
    return render_template('reg_course.html', dep_list = dep_list, course_list=course_list)

# insert department
@register_route.route('/course', methods=['POST'])
@login_required
def reg_course():
    cour_name = request.form.get('course_name')
    cour_dep = request.form.get('course_dep')
    Reg_course.insert_reg(cour_name, cour_dep)
    flash('Cadastro Realizado com Sucesso')
    return redirect(url_for('register.course_list'))

# delete
@register_route.route('/course/<id>', methods=['POST'])
@login_required
def course_del(id):
    Reg_course.delete_reg(id)
    flash('Operação realizado com sucesso')
    return redirect(url_for('register.course_list'))


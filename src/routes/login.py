from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.entities.users import Users
from .. import db, login_manager
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
login_route = Blueprint('login', __name__)

@login_manager.user_loader
def loader_user(user_id):
    return Users.query.filter_by(userid=user_id).first()

@login_route.route('/', methods=['POST'])
def login_authentication():
    titulo = "Página de Login"
    if request.method =="POST":
        user_name = request.form.get('username')
        password = request.form.get('userpassword')
        remember = True if request.form.get('rememberme') else False
        #print(f"Inserido, usuário: {user_name} e senha: {password}!")
        user = Users.query.filter_by(userid=user_name).first()#Users.query.filter_by(username=user_name).first()
        
        if not user.userid or not user.check_password(password) :#and bcrypt.check_password_hash(user.userpassword, password):            
            flash('Please check your login details and try again.')
            return redirect(url_for('login.login_form'))       
    else:
        return "Erro no login"
    user.authenticated = True
    db.session.add(user)
    db.session.commit()
    login_user(user, remember=remember)
    return redirect(url_for('users.list_users'))


@login_route.route('/', methods=['GET'])
def login_form():
    return render_template('login.html')

@login_route.route('/logout', methods=['GET'])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    print("{user.userid}")
    user.authenticated =False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template('login.html')

@login_manager.unauthorized_handler
def unauthorized():
    if request.blueprint == 'api':
        abort(HTTPStatus.UNAUTHORIZED)
    return redirect(url_for('login.login_form'))

"""
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print('Received data:', username , password)

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'Login Success', 'access_token': access_token})
    else:
        return jsonify({'message': 'Login Failed'}), 401
"""
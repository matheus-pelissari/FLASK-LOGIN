# ----------------------------- USUÁRIOS -----------------------------

from flask import Blueprint, request, render_template
import flask_login
from flask_login import LoginManager
import flask

login = Blueprint("login",__name__, template_folder="templates")

login_manager = LoginManager()
login_manager.login_view = 'login.logando'

usuarios = {'user1': {'password':'1234'},'user2': {'password':'1234'}}


class User(flask_login.UserMixin):
    def __init__(self, user_id):
        self.id = user_id
    
    def get_id(self):
        return self.id

@login_manager.user_loader
def user_loader(username):
    if username not in usuarios:
        return
    user = User(username)
    user.id = username
    return user

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('usuario')
    if username not in usuarios:
        return
    user = User(username)
    user.id = username
    return user


@login.route('/login', methods=['GET', 'POST'])
def logando():
    if flask.request.method == 'GET':
        return render_template("login.html")
    username = flask.request.form['usuario']
    if username in usuarios and flask.request.form['password'] == usuarios[username]['password']:
        user = User(username)
        user.id = username
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('home'))
    return 'Bad Login'


@login.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


@login.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return render_template("login.html")


# Apenas definindo a rota para a pagina HTML de registrar.
@login.route('/registrar_usuario')
@flask_login.login_required
def register_user():
    return render_template("registrar_usuario.html")


# Aqui realmente ocorre o registro 
@login.route('/add_user', methods = ['GET', 'POST'])
def add_user():
    global usuarios
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
    else:
        # Se for GET lê user e password nos query params da URL 
        usuario = request.args.get('usuario', None)
        password = request.args.get('password', None)
    # Insere no dicionario
    usuarios[usuario] = {'password': password}
    return render_template("listar_usuarios.html", usuarios = usuarios)


@login.route('/listar_usuarios')
@flask_login.login_required
def list_users():
    global usuarios
    return render_template("listar_usuarios.html", usuarios = usuarios)


@login.route('/remover_usuario')
@flask_login.login_required
def remove_user():
    return render_template("remover_usuario.html", usuarios = usuarios)


@login.route('/del_user', methods = ['GET', 'POST'])
@flask_login.login_required
def del_user():
    global usuarios
    if request.method == "POST":
        usuario = request.form['usuario']
    else:
        usuario = request.args.get('usuario', None)
    usuarios.pop(usuario)
    return render_template("listar_usuarios.html", usuarios = usuarios)
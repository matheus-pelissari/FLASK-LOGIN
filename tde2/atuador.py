# ----------------------------- ATUADORES -----------------------------

from flask import Blueprint, request, render_template
from flask_login import login_required, current_user 
atuadorr = Blueprint("atuadorr",__name__, template_folder="templates")

atuadores = {'Teste4':4, 'Teste5':5, 'Teste6':6}


@atuadorr.route('/registrar_atuador')
@login_required
def register_actuator(): 
    return render_template("registrar_atuador.html")


@atuadorr.route('/add_atuador', methods = ['GET', 'POST'])
def add_atuador():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
        valor_a = request.form['valor_a']
    else:
        atuador = request.args.get('atuador', None)
        valor_a = request.args.get('valor_a', None)
    atuadores[atuador] = valor_a
    return render_template("listar_atuadores.html", atuadores = atuadores)


@atuadorr.route("/listar_atuadores")
@login_required
def actuator():
    return render_template("listar_atuadores.html", atuadores = atuadores)


@atuadorr.route('/remover_atuador')
@login_required
def remove_atuador():
    return render_template("remover_atuador.html", atuadores = atuadores)


@atuadorr.route('/del_atuador', methods = ['GET', 'POST'])
def del_atuador():
    global atuadores
    if request.method == "POST":
        atuador = request.form['atuador']
    else:
        atuador = request.args.get['atuador', None]
    atuadores.pop(atuador)
    return render_template("listar_atuadores.html", atuadores = atuadores)

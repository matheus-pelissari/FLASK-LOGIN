# ----------------------------- SENSORES -----------------------------

from flask import Blueprint, request, render_template
from flask_login import login_required, current_user  

sensorss = Blueprint("sensorss",__name__, template_folder="templates")

sensores = {'Teste1':1, 'Teste2':2, 'Teste3':3}


@sensorss.route('/registrar_sensor')
@login_required
def register_sensor():
    return render_template("registrar_sensor.html")


@sensorss.route('/add_sensor', methods = ['GET', 'POST'])
def add_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
        valor = request.form['valor']
    else:
        # Se for GET lê user e password nos query params da URL 
        sensor = request.args.get('sensor', None)
        valor = request.args.get('valor', None)
    # Insere no dicionario
    sensores[sensor] = valor
    return render_template("listar_sensores.html", sensores = sensores)


@sensorss.route("/listar_sensores")
@login_required
def sensors():
    global sensores
    return render_template("listar_sensores.html", sensores = sensores)


@sensorss.route('/remover_sensor')
@login_required
def remove_sensor():
    return render_template("remover_sensor.html", sensores = sensores)


@sensorss.route('/del_sensor', methods = ['GET', 'POST'])
def del_sensor():
    global sensores
    if request.method == "POST":
        sensor = request.form['sensor']
    else:
        sensor = request.args.get['sensor', None]
    sensores.pop(sensor)
    return render_template("listar_sensores.html", sensores = sensores)
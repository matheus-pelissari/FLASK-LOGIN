from flask import Flask, render_template, request
from login import login, login_manager
from sensor import sensorss
from atuador import atuadorr


# Objeto python :  __name__ é o nome do aplicação.
app = Flask(__name__)
app.secret_key = 'chave secreta'

login_manager.init_app(app)
login_manager.login_view = 'login.logando'

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensorss, url_prefix='/')
app.register_blueprint(atuadorr, url_prefix='/')


@app.route('/')
def index():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)
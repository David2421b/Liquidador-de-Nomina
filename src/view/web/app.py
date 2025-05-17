import sys

sys.path.append(".")

from flask import Flask
from flask import render_template, request

from src.controller.nomina_controller import NominaController
from model.calculo_nomina import Nomina
from model.clase_empleado import Empleado

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pagina_registro")
def pagina_registrar():
    return render_template("registrar.html")

@app.route("/acceder", methods = ["GET", "POST"])
def acceder():
    if request.method == "POST":
        cedula = request.form["cedula"]
        
        nomina = Nomina()


if __name__ == "__main__":
    app.run(debug = True)
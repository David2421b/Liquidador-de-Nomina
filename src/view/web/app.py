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

@app.route("/registrar", methods = ["GET", "POST"])
def registrar():
    if request.method == "POST":
        cedula = request.form["cedula"]
        nombre = request.form["nombres"]
        apellido = request.form["apellidos"]
        cargo = request.form["cargo"]
        salario_base = request.form["salario_base"]
        horas_extra = request.form["horas_extras"]
        tipo_hora_extra = request.form["tipo_hora_extra"]
        horas_extras_adicionales = request.form["horas_extras_adicionales"]
        tipo_hora_extra_adicionales = request.form["tipo_hora_extra_adicional"]
        prestamo = request.form["prestamo"]
        cuotas = request.form["cuotas"]
        tasa_interese = request.form["tasa_interes_anual"]

        nomina = Nomina(cedula_empleado = cedula, nombre_empleado = nombre, empleado_apellido = apellido, cargo = cargo,
                        salario_base = salario_base, horas_extras = horas_extra, tipo_hora_extra = tipo_hora_extra,
                        horas_extras_adicionales = horas_extras_adicionales, tipo_hora_extra_adicional = tipo_hora_extra_adicionales,
                        prestamo = prestamo, cuotas = cuotas, tasa_interes = tasa_interese)
        return render_template("index.html")

@app.route("/acceder", methods = ["GET", "POST"])
def acceder():
    ...

if __name__ == "__main__":
    app.run(debug = True)
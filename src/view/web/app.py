import sys

sys.path.append(".")

from flask import Flask
from flask import render_template, request

from src.controller.nomina_controller import NominaController
from model.calculo_nomina import Nomina


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
        salario_base = float(request.form["salario_base"])
        horas_extra = int(request.form["horas_extras"])
        tipo_hora_extra = request.form["tipo_hora_extra"]
        horas_extras_adicionales = int(request.form["horas_extras_adicionales"])
        tipo_hora_extra_adicional = request.form["tipo_hora_extra_adicional"]
        prestamo = float(request.form["prestamo"])
        cuotas = int(request.form["cuotas"])
        tasa_interese = float(request.form["tasa_interes_anual"])
        print("entre1")

        nomina = Nomina(cedula_empleado = cedula, nombre_empleado = nombre, empleado_apellido = apellido, cargo = cargo,
                        salario_base = salario_base, horas_extras = horas_extra, tipo_hora_extra = tipo_hora_extra,
                        horas_extras_adicionales = horas_extras_adicionales, tipo_hora_extra_adicional = tipo_hora_extra_adicional,
                        prestamo = prestamo, cuotas = cuotas, tasa_interes = tasa_interese)
        
        NominaController.InsertarNomina(nomina)
        try:
            print("entre2")
            return render_template("index.html", mensaje = f"el usuarios: '{nombre}' se ha registrado con exito")
        
        except Exception as e:
            return render_template("registrar.html", mensaje = f"el usuario: '{nombre}' no se registro con exito debido a: {str(e)}")

@app.route("/acceder", methods = ["GET", "POST"])
def acceder():
    if request.method == "POST":
        cedula = request.form["cedula"]
        try:
            usuario_buscado = NominaController.ObtenerEmpleadoPorCedula(cedula)
            if usuario_buscado and usuario_buscado["cedula"] == cedula:
                return render_template("panel.html")
            
        except Exception as e:
                return render_template("index.html", mensaje = f"La cedula: {cedula} no se encuentra registrada")


if __name__ == "__main__":
    app.run(debug = True)
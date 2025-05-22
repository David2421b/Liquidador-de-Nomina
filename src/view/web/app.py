import sys

sys.path.append(".")

from flask import Flask
from flask import render_template, request

from src.controller.nomina_controller import NominaController
from model.calculo_nomina import Nomina


app = Flask(__name__)

@app.route("/")
def index():
    NominaController.CrearTablas()
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

        nomina = Nomina(cedula_empleado = cedula, nombre_empleado = nombre, empleado_apellido = apellido, cargo = cargo,
                        salario_base = salario_base, horas_extras = horas_extra, tipo_hora_extra = tipo_hora_extra,
                        horas_extras_adicionales = horas_extras_adicionales, tipo_hora_extra_adicional = tipo_hora_extra_adicional,
                        prestamo = prestamo, cuotas = cuotas, tasa_interes = tasa_interese)
        
        try:
            # NominaController.InsertarNomina(nomina)
            salario_neto_obtenido = nomina.calcular()
            bonifiacion_obetenido = nomina.calcular_bonificacion()
            valor_horas_extra_obtenido = nomina.calcular_valor_hora_extra(nomina.horas_extras, nomina.tipo_hora_extra)
            valor_hora_extra_adicional_obtenida = nomina.calcular_valor_hora_extra(nomina.horas_extras_adicionales, nomina.tipo_hora_extra_adicional)
            total_horas_extra_obtenido = (valor_horas_extra_obtenido * nomina.horas_extras) + (valor_hora_extra_adicional_obtenida * nomina.horas_extras_adicionales)

            return render_template("panel.html", cedula = cedula, nombre = nombre, apellido = apellido, cargo = cargo,
                                                    salario_base = salario_base, bonificacion_cargo = bonifiacion_obetenido,
                                                    horas_extra = horas_extra, tipo_horas_extra = tipo_hora_extra,
                                                    horas_extra_adicionales = horas_extras_adicionales,
                                                    tipo_horas_extra_adicional = tipo_hora_extra_adicional,
                                                    valor_hora_extra = total_horas_extra_obtenido, prestamo = prestamo,
                                                    cuotas = cuotas, tasa_interes = tasa_interese,
                                                    salario_neto = salario_neto_obtenido)
        
        except Exception as e:
            return render_template("registrar.html", mensaje = f"el usuario: '{nombre}' no se registro con exito debido a: '{str(e)}'")

@app.route("/acceder", methods = ["GET", "POST"])
def acceder():
    if request.method == "POST":
        cedula = request.form["cedula"]
        try:
            usuario_buscado = NominaController.ObtenerEmpleadoPorCedula(cedula)
            return render_template("index.html", usuario_buscado = f"Cedula: {usuario_buscado['cedula']}, Nombre: {usuario_buscado['nombres']} {usuario_buscado['apellidos']}")
            
            
        except Exception as e:
                return render_template("index.html", mensaje = f"{e}")


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8080)
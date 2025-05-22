import sys

sys.path.append(".")

from flask import Flask
from flask import render_template, request

from src.controller.nomina_controller import NominaController
from model.calculo_nomina import Nomina
from model.clase_datos_obtenidos import DatosObtenidos


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

        try:

            nomina = Nomina(cedula_empleado = cedula, nombre_empleado = nombre, empleado_apellido = apellido, cargo = cargo,
                            salario_base = salario_base, horas_extras = horas_extra, tipo_hora_extra = tipo_hora_extra,
                            horas_extras_adicionales = horas_extras_adicionales, tipo_hora_extra_adicional = tipo_hora_extra_adicional,
                            prestamo = prestamo, cuotas = cuotas, tasa_interes = tasa_interese)
        
            NominaController.InsertarNomina(nomina)
            salario_neto_obtenido = nomina.calcular()
            bonifiacion_obetenido = nomina.calcular_bonificacion()
            valor_horas_extra_obtenido = nomina.calcular_valor_hora_extra(nomina.horas_extras, nomina.tipo_hora_extra)
            valor_hora_extra_adicional_obtenida = nomina.calcular_valor_hora_extra(nomina.horas_extras_adicionales, nomina.tipo_hora_extra_adicional)
            total_horas_extra_obtenido = (valor_horas_extra_obtenido * nomina.horas_extras) + (valor_hora_extra_adicional_obtenida * nomina.horas_extras_adicionales)

            datos_obtenidos = DatosObtenidos(cedula, salario_neto_obtenido, bonifiacion_obetenido, total_horas_extra_obtenido)
            NominaController.InsertarDatosObtenidos(datos_obtenidos)

            return render_template("index.html", mensaje = "Usuario registrado con exito")
        
        except Exception as e:
            print("Entre")
            return render_template("registrar.html", mensaje = f"el usuario: '{nombre}' no se registro con exito debido a: '{str(e)}'")

@app.route("/acceder", methods = ["GET", "POST"])
def acceder():
    if request.method == "POST":
        cedula = request.form["cedula"]
        try:
            usuario_buscado = NominaController.ObtenerEmpleadoPorCedula(cedula)
            datos_usuario_buscados = NominaController.ObtenerDatosExtraEmpleado(cedula)
            print(datos_usuario_buscados)
            if usuario_buscado["cedula"] == cedula:
                # return render_template("panel.html")

                return render_template("panel.html", cedula = usuario_buscado["cedula"], nombre = usuario_buscado["nombres"],
                                                    apellido = usuario_buscado["apellidos"], cargo = usuario_buscado["cargo"],
                                                    salario_base = usuario_buscado["salario_base"], bonificacion = datos_usuario_buscados.bonificacion,
                                                    horas_extra = usuario_buscado["horas_extras"],
                                                    valor_hora_extra = datos_usuario_buscados.valor_hora_extra, prestamo = usuario_buscado["prestamo"],
                                                    cuotas = usuario_buscado["cuotas"], tasa_interes = usuario_buscado["tasa_interes_anual"],
                                                    salario_neto = datos_usuario_buscados.salario_neto)
            
        except Exception as e:
                # return render_template("index.html", mensaje = f"La cedula: {cedula} no se encuentra registrada")
                return render_template("index.html", mensaje = f"{e}")


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8080)



    #terminar la nueva tabla y agragarla al controller, tambien crear la clase para insertarla
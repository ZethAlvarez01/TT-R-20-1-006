from flask import Flask, render_template,request,make_response,json
from flask import send_file, send_from_directory
from Validacion import validacion
from Error_signos import error_signos
from Evalua_palabras import evalua_palabra
from buscar_significado import buscar_significado
from descargar import descargar
from Buscar_sugerencias import buscar_sug
from Evalua_frases import evalua_frases
from datetime import date

app = Flask(__name__)

# Index Pantalla principal
@app.route('/')
def index():
    return render_template('index.html')

# Verifica la escructura de las oraciones 
@app.route('/oraciones_validar/<string:texto>/')
def oraciones_validar(texto):
    return json.jsonify({
        'arreglo_pruebas': evalua_frases(texto)
    })

# Valida el uso de mayusculas, minusculas y numeros
@app.route('/validacion_minusculas_mayusculas/<string:texto>/')
def background_process_test(texto):
    return json.jsonify({
        'lista': validacion(texto)
    })

# Valida el uso de signos de puntuacion
@app.route('/validacion_signos/<string:texto>/')
def background_process_test2(texto):
    return json.jsonify({
        'aerr': error_signos(texto)
    })

# Valida palabra con el diccionario, regresa si esta correcta o no
@app.route('/validar_palabra/<string:texto>/')
def validar_palabra(texto):
    return json.jsonify({
        'validar': evalua_palabra(texto)
    })

#Encuentra las sugerencias de las palabras mal escritas
@app.route('/buscar_sugerencias/<string:textsn>/')
def buscar_sugerencias(textsn):
    return json.jsonify({
        'sugerencia': buscar_sug(textsn)
    })

# Descarga el texto en archivos pdf y txt
@app.route('/return_file/<texto>/<opcion>/<Errores_rojosC>/<Errores_azulesC>/<Errores_moradosC>')
def return_file(texto,opcion,Errores_rojosC,Errores_azulesC,Errores_moradosC):
    return descargar(texto,opcion,Errores_rojosC,Errores_azulesC,Errores_moradosC)


if __name__ == '__main__':
    app.run()
    
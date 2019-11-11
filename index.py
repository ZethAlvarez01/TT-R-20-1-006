from flask import Flask, render_template,request,make_response,json
from flask import send_file, send_from_directory
from Validacion import validacion
from Error_signos import error_signos
from Evalua_palabras import evalua_palabra
from buscar_significado import buscar_significado
from descargar import descargar
from datetime import date

app = Flask(__name__)

# Index Pantalla principal
@app.route('/')
def index():
    return render_template('index.html')

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

# Busca el significado de alguna palabra en la web (No corriendo)
@app.route('/buscar_palabra/<string:texto>/')
def buscar_palabra(texto):
    return json.jsonify({
        'palabra': buscar_significado(texto)
    })

# Valida palabra con el diccionario, regresa si esta correcta o no
@app.route('/validar_palabra/<string:texto>/')
def validar_palabra(texto):
    return json.jsonify({
        'validar': evalua_palabra(texto)
    })

# Descarga el texto en archivos Pdf y txt
@app.route('/return_file/<texto>/<opcion>/<Thtml>')
def return_file(texto,opcion,Thtml):
    return descargar(texto,opcion,Thtml)


if __name__ == '__main__':
    app.run(debug=True, port=8101)
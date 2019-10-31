from flask import Flask, render_template,request,make_response,json
from flask import send_file, send_from_directory
from Principal import validacion
from Puntuacion import error_signos
from buscar_significado import buscar_significado
from descargar import descargar
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validacion_minusculas_mayusculas/<string:texto>/')
def background_process_test(texto):
    return json.jsonify({
        'lista': validacion(texto)
    })

@app.route('/validacion_signos/<string:texto>/')
def background_process_test2(texto):
    return json.jsonify({
        'aerr': error_signos(texto)
    })

@app.route('/buscar_palabra/<string:texto>/')
def buscar_palabra(texto):
    return json.jsonify({
        'palabra': buscar_significado(texto)
    })

@app.route('/return_file/<texto>/<opcion>')
def return_file(texto,opcion):
    return descargar(texto,opcion)


if __name__ == '__main__':
    app.run(debug=True, port=9850)
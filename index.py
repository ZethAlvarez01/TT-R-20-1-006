from tkinter import filedialog, Tk
from flask import Flask, render_template,request,make_response,json
from flask import send_file, send_from_directory
from Principal import validacion
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/background_process_test/<string:texto>/')
def background_process_test(texto):
    return json.jsonify({
        'lista': validacion(texto)
    })

@app.route('/return_file/<texto>/<opcion>')
def return_file(texto,opcion):

    root = Tk()
    root.withdraw()
    directorio = filedialog.askdirectory()
    #directorio = eg.diropenbox(title="Seleccionar ruta",default='/home/')

    if opcion == "1":
        c = canvas.Canvas(directorio + '/Prototipo_de_asistente_corrector_gramatical_y_ortográfico.pdf',pagesize=A4)
        c.drawString(50,800, texto)
        c.save()
        return "nothing"
    else:
        file = open(directorio + "/Prototipo_de_asistente_corrector_gramatical_y_ortográfico_ruta.txt", "w")
        file.write(texto)
        file.close()
        return "nothing"
    


if __name__ == '__main__':
    app.run(debug=True, port=9422)

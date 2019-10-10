from flask import Flask, render_template,request,make_response,json
from Principal import validacion
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def get_text():
    text=request.form.get("text")
    pdf=pdfkit.from_string(text,False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=TT-R-20-1-006.pdf'
    return response

@app.route('/background_process_test/<string:texto>/')
def background_process_test(texto):
    return json.jsonify({
        'lista': validacion(texto)
    })

if __name__ == '__main__':
    app.run(debug=True, port=9156)

from flask import Flask, render_template,request
from reportlab.pdfgen import canvas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def get_text():
    text=request.form.get("text")
    c = canvas.Canvas("tt-r-20-1-006.pdf")
    c.drawString(50, 50, text)
    c.save()
    return c

if __name__ == '__main__':
    app.run(debug=True, port=8555)

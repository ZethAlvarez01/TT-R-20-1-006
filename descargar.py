from flask import Flask, render_template,request,make_response,json
from flask import send_file, send_from_directory
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from datetime import date

def descargar(texto,opcion):
    if(opcion == '1'):
        c = canvas.Canvas("static/files/Texto_corregido_"+ date.today().strftime("%d-%B-%y") +".pdf")
        c.drawString(50, 800, texto)
        c.save()
        return send_file('static/files/Texto_corregido_'+ date.today().strftime("%d-%B-%y") +'.pdf',attachment_filename="Texto_corregido_"+ date.today().strftime("%d-%B-%y") +".pdf",as_attachment=True)
    else:
        archivo = open("static/files/Texto_corregido_"+ date.today().strftime("%d-%B-%y") +".txt", "w") 
        archivo.write(texto)
        archivo.close()
        return send_file('static/files/Texto_corregido_'+ date.today().strftime("%d-%B-%y") +'.txt',attachment_filename="Texto_corregido_"+ date.today().strftime("%d-%B-%y") +".txt",as_attachment=True)
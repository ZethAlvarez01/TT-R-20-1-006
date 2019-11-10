from flask import Flask, render_template,request,make_response,json
from flask import send_file, send_from_directory
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import date
import time

def descargar(texto,opcion):

    variablee = texto
    if(opcion == '1'):
        doc = SimpleDocTemplate("static/files/Texto_corregido_"+ date.today().strftime("%d-%B-%y") +".pdf", pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)
        Story = []

        estilos = getSampleStyleSheet()
        estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

        estilos2 = getSampleStyleSheet()
        estilos2.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

        texto = '%s' % date.today().strftime("%d-%B-%y")
        Story.append(Paragraph(texto, estilos["Normal"]))
        Story.append(Spacer(1, 12))


        texto = "Prototipo de asistente corrector gramatical y ortográfico"
        Story.append(Paragraph(texto, estilos2["Center"]))
        texto = "  "
        Story.append(Paragraph(texto, estilos2["Center"]))
        texto = "  "
        Story.append(Paragraph(texto, estilos2["Center"]))
        
    
        Story.append(Paragraph(variablee, estilos["Justify"]))
        Story.append(Spacer(1, 12))

        texto = "  "
        Story.append(Paragraph(texto, estilos2["Center"]))
        texto = "  "
        Story.append(Paragraph(texto, estilos2["Center"]))
        texto = "  "
        Story.append(Paragraph(texto, estilos2["Center"]))
        
        texto = '\n\n\nInstituto Politécnico Nacional'
        Story.append(Paragraph(texto, estilos["Justify"]))
        Story.append(Spacer(1, 12))
        texto = 'Escuela superior de cómputo'
        Story.append(Paragraph(texto, estilos["Normal"]))
        Story.append(Spacer(1, 48))
        
        doc.build(Story)

        return send_file('static/files/Texto_corregido_'+ date.today().strftime("%d-%B-%y") +'.pdf',attachment_filename="Texto_corregido_"+ date.today().strftime("%d-%B-%y") +".pdf",as_attachment=True)
    else:
        archivo = open("static/files/Texto_corregido_"+ date.today().strftime("%d-%B-%y") +".txt", "w") 
        archivo.write(texto)
        archivo.close()
        return send_file('static/files/Texto_corregido_'+ date.today().strftime("%d-%B-%y") +'.txt',attachment_filename="Texto_corregido_"+ date.today().strftime("%d-%B-%y") +".txt",as_attachment=True)
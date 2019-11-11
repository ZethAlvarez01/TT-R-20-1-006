from flask import Flask, render_template,request,make_response,json
from flask import send_file, send_from_directory
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import date
import time

def descargar(texto,opcion,Errores_rojosC,Errores_azulesC,Errores_moradosC):

    rojos = Errores_rojosC.split("|")
    azules = Errores_azulesC.split("|")
    morados = Errores_moradosC.split("|")

    print("Errores r")
    print(rojos)
    print("Errores a")
    print(azules)
    print("Errores m")
    print(morados)


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

        estilos3 = getSampleStyleSheet()
        estilos3.add(ParagraphStyle(name='Left', alignment=TA_LEFT))

        estilos4 = getSampleStyleSheet()
        estilos4.add(ParagraphStyle(name='Color', textColor="red"))

        texto = '%s' % date.today().strftime("%d-%B-%y")
        Story.append(Paragraph(texto, estilos["Normal"]))
        Story.append(Spacer(1, 12))


        texto = "Prototipo de asistente corrector gramatical y ortográfico"
        Story.append(Paragraph(texto, estilos2["Center"]))
        Story.append(Spacer(1, 30))
        
        texto = "Texto evaluado: "
        Story.append(Paragraph(texto, estilos4["Color"]))
        Story.append(Spacer(1, 30))
    
        Story.append(Paragraph(variablee, estilos["Justify"]))
        Story.append(Spacer(1, 30))


        if(len(rojos)-2 != 0 or len(azules)-2 != 0 or len(morados)-2):
            texto = "Este documento aún posee errores. Se listan a continuación: "
            Story.append(Paragraph(texto, estilos4["Color"]))
            Story.append(Spacer(1, 15))
            
            if(len(rojos)-2 != 0):
                texto = "- Errores en uso de mayúsculas y minúsculas "
                Story.append(Paragraph(texto, estilos["Justify"]))
                for palr in rojos:
                    Story.append(Paragraph(palr, estilos3["Left"]))
                    Story.append(Spacer(1, 5))

            if(len(azules)-2 != 0):
                texto = "- Errores en uso de signos de puntuación "
                Story.append(Paragraph(texto, estilos["Justify"]))
                for pala in azules:
                    Story.append(Paragraph(pala, estilos3["Left"]))
                    Story.append(Spacer(1, 5))

            if(len(morados)-2 != 0):
                texto = "- Palabras no encontradas en el diccionario "
                Story.append(Paragraph(texto, estilos["Justify"]))
                for palm in morados:
                    Story.append(Paragraph(palm, estilos3["Left"]))
                    Story.append(Spacer(1, 5))


        Story.append(Spacer(1, 30))
        
        texto = 'Instituto Politécnico Nacional'
        Story.append(Paragraph(texto, estilos["Normal"]))
        texto = 'Escuela superior de cómputo'
        Story.append(Paragraph(texto, estilos["Normal"]))
        
        doc.build(Story)

        return send_file('static/files/Texto_corregido_'+ date.today().strftime("%d-%B-%y") +'.pdf',attachment_filename="Texto_corregido_"+ date.today().strftime("%d-%B-%y") +".pdf",as_attachment=True)
    else:
        archivo = open("static/files/Texto_corregido_"+ date.today().strftime("%d-%B-%y") +".txt", "w") 
        archivo.write(texto)
        archivo.close()
        return send_file('static/files/Texto_corregido_'+ date.today().strftime("%d-%B-%y") +'.txt',attachment_filename="Texto_corregido_"+ date.today().strftime("%d-%B-%y") +".txt",as_attachment=True)
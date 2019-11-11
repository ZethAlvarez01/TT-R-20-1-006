from flask import Flask, render_template,request,make_response,json
from flask import send_file, send_from_directory
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import date
from html.parser import HTMLParser
import time

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)


def descargar(texto,opcion,Thtml):

    #print(Thtml)

    Thtml = Thtml.replace("|","/",len(Thtml))

    print(Thtml)

    parser = MyHTMLParser()
    parser.feed(Thtml)

    print(parser)

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
        texto = "----"
        Story.append(Paragraph(texto, estilos2["Center"]))
        texto = "----"
        Story.append(Paragraph(texto, estilos2["Center"]))
        
    
        Story.append(Paragraph(variablee, estilos["Justify"]))
        Story.append(Spacer(1, 12))

        texto = "-----"
        Story.append(Paragraph(texto, estilos2["Center"]))
        texto = "-----"
        Story.append(Paragraph(texto, estilos2["Center"]))
        texto = "-----"
        Story.append(Paragraph(texto, estilos2["Center"]))
        
        texto = 'nInstituto Politécnico Nacional'
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
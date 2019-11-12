def evalua_frases(cadena):
    cadena = "Este reporte presenta el avance de la propuesta e implementación de un prototipo de asistente corrector " \
         "gramatical y ortográfico para la redacción de protocolos gramaticalmente correctos, basado en la " \
         "arquitectura orientada a servicios, denominada software como servicio o SaaS por sus siglas en inglés. "
    arr = []
    arrep = []
    arren = []
    respuesta = ""
    ef = [2, 3, 4, 5, 7, 9]  # Estados finales
    signos = ['-', ',', ':', ';', '¿', '?', '¡', '!', '"', ' '] # Signos que no afectan
    signosf = ['.', '?', '!'] # Signos que afectan
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    j = len(cadena)
    palabras = []
    cad = ""
    #   Aqui se separan las palabras que se van a analizar
    for i in range(j):
        flg = cadena[i].isspace()
        if cadena[i].islower() is True or cadena[i].isupper() is True or \
                num.__contains__(cadena[i]) is True:
            cad = cad + cadena[i].lower()
        elif cadena[i].isspace() is True and len(cad) != 0:
            palabras.append(cad)
            cad = ""
            palabras.append(cadena[i])
        elif cadena[i].isspace() is True and len(cad) == 0:
            palabras.append(cadena[i])
        elif cadena[i].islower() is False and cadena[i].isupper() is False and \
                num.__contains__(cadena[i]) is False:
            if len(cad) != 0:
                palabras.append(cad)
                cad = ""
            palabras.append(cadena[i])
    if cad != " " and len(cad) != 0:
        if cad != 0:
            palabras.append(cad)
    #   Aqui se lee el documento de las etiquetas
    doc = open("Diccionario_de_palabras/Etiquetado.txt", 'r')
    for linea in doc.readlines():
        x = linea.split("/")
        arrep.append(x[0])
        arren.append(x[1].__getitem__(0))
    doc.close()
    #   Aqui se busca la categoría de las palabras
    for h in range(len(palabras)):
        for r in range(len(arrep)):
            if palabras[h] == arrep[r]:
                arr.append(arren[r])
                break
            elif signos.__contains__(palabras[h]):
                arr.append(0)
                break
            elif signosf.__contains__(palabras[h]):
                arr.append(1)
                break
            elif palabras[h] is '(':
                arr.append(2)
                break
            elif palabras[h] is ')':
                arr.append(3)
                break
            elif r == len(arrep) -1:
                arr.append('D')
                break

    pos = 0
    flg = 0
    h = pos
    hflg = 0
    print(arr)

    for i in range(len(arr)):

        if pos == 0:
            if arr[i] is 'A' or arr[i] is 'F':
                pos = 1
            elif arr[i] is 'B':
                pos = 2
            elif arr[i] is 'C':
                pos = 7
            elif arr[i] is 'D':
                pos = 12
            elif arr[i] is 'E':
                pos = 6
            elif arr[i] is 'G':
                pos = 11
            elif arr[i] is 'H':
                pos = 10

        elif pos == 1:
            if arr[i] is 'A' or arr[i] is 'C' or arr[i] is 'D' or arr[i] is 'E' or arr[i] is 'F' or arr[i] is 'G' \
                    or arr[i] is 'H':
                pos = -1
            elif arr[i] is 'B':
                pos = 2

        elif pos == 2:
            if arr[i] is 'A':
                pos = 1
            elif arr[i] is 'B' or arr[i] is 'E' or arr[i] is 'H':
                pos = 2
            elif arr[i] is 'C':
                pos = 3
            elif arr[i] is 'D':
                pos = 5
            elif arr[i] is 'F':
                pos = 4
            elif arr[i] is 'G':
                pos = 9

        elif pos == 3:
            if arr[i] is 'A':
                pos = 1
            elif arr[i] is 'B':
                pos = 2
            elif arr[i] is 'C':
                pos = 3
            elif arr[i] is 'D':
                pos = 5
            elif arr[i] is 'E' or arr[i] is 'F' or arr[i] is 'H':
                pos = -1
            elif arr[i] is 'G':
                pos = 9

        elif pos == 4:
            if arr[i] is 'A':
                pos = 1
            elif arr[i] is 'B':
                pos = 2
            elif arr[i] is 'C':
                pos = 3
            elif arr[i] is 'D':
                pos = 5
            elif arr[i] is 'E' or arr[i] is 'G' or arr[i] is 'H':
                pos = -1
            elif arr[i] is 'F':
                pos = 4

        elif pos == 5:
            if arr[i] is 'A':
                pos = 1
            elif arr[i] is 'B':
                pos = 2
            elif arr[i] is 'C' or arr[i] is 'E' or arr[i] is 'H':
                pos = -1
            elif arr[i] is 'D':
                pos = 5
            elif arr[i] is 'F':
                pos = 4
            elif arr[i] is 'G':
                pos = 9

        elif pos == 6:
            if arr[i] is 'A':
                pos = 1
            elif arr[i] is 'B':
                pos = 2
            elif arr[i] is 'C':
                pos = 7
            elif arr[i] is 'D' or arr[i] is 'E' or arr[i] is 'F':
                pos = -1
            elif arr[i] is 'G':
                pos = 8
            elif arr[i] is 'H':
                pos = 2

        elif pos == 7:
            if arr[i] is 'A':
                pos = 1
            elif arr[i] is 'B':
                pos = 2
            elif arr[i] is 'C':
                pos = 7
            elif arr[i] is 'D':
                pos = 4
            elif arr[i] is 'E' or arr[i] is 'F' or arr[i] is 'G':
                pos = -1
            elif arr[i] is 'H':
                pos = 10

        elif pos == 8:
            if arr[i] is 'A' or arr[i] is 'B' or arr[i] is 'D' or arr[i] is 'E' or arr[i] is 'F' or arr[i] is 'G' \
                    or arr[i] is 'H':
                pos = -1
            elif arr[i] is 'C':
                pos = 7

        elif pos == 9:
            if arr[i] is 'A' or arr[i] is 'B' or arr[i] is 'D' or arr[i] is 'E' or arr[i] is 'F' or arr[i] is 'G' \
                    or arr[i] is 'H':
                pos = -1
            elif arr[i] is 'C':
                pos = 3

        elif pos == 10:
            if arr[i] is 'A':
                pos = 1
            elif arr[i] is 'B':
                pos = 2
            elif arr[i] is 'C':
                pos = 7
            elif arr[i] is 'D' or arr[i] is 'E' or arr[i] is 'F' or arr[i] is 'H':
                pos = -1
            elif arr[i] is 'G':
                pos = 8

        elif pos == 11:
            if arr[i] is 'A' or arr[i] is 'B' or arr[i] is 'D' or arr[i] is 'E' or arr[i] is 'F' or arr[i] is 'G' \
                    or arr[i] is 'H':
                pos = -1
            elif arr[i] is 'C':
                pos = 7

        elif pos == 12:
            if arr[i] is 'A':
                pos = 1
            elif arr[i] is 'B':
                pos = 2
            elif arr[i] is 'C' or arr[i] is 'E' or arr[i] is 'F' or arr[i] is 'G' or arr[i] is 'H':
                pos = -1
            elif arr[i] is 'D':
                pos = 12

        elif pos == -1 and flg == 0:
            flg = 1
            print("Tu error se originó en la palabra: %d" % i)

        # Si encuentra un signo de puntuación, reinicia el autómata
        elif arr[i] == 1:
            if ef.__contains__(pos) is False:
                respuesta = "Tu estado (%d) no es un estado final, por lo que la oración está mal." % pos
                print("Tu estado (%d) no es un estado final, por lo que la oración está mal." % pos)
            pos = 0
            flg = 0
        # Si encuentra un ( reinicia el autómata pero guarda la ultima posición
        elif arr[i] == 2:
            h = pos
            pos = 0
            hflg = flg
            flg = 0
        # Si encuentra un ) termina el ciclo del autómata y retoma el ciclo anterior hasta el punto en que se había quedado
        elif arr[i] == 3:
            if ef.__contains__(pos) is False:
                respuesta = "Tu estado (%d) no es un estado final, por lo que la oración está mal." % pos
                print("Tu estado (%d) no es un estado final, por lo que la oración está mal." % pos)
            pos = h
            h = 0
            flg = hflg
            hflg = 0
        print("%i: %s, %i" % (h, arr[i], pos))

    if ef.__contains__(pos) is True:
        respuesta = "Felicidades, tu cadena se escribió con exito!"
        print("Felicidades, tu cadena se escribió con exito!")
    #print(palabras)
    #print(arr)
    return respuesta
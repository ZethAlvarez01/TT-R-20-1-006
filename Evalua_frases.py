def evalua_frases(cadena):
    
    arr = []
    arrep = []
    arren = []
    ef = [2, 3, 4, 5, 7, 9]  # Estados finales
    signos = ['-', ',', ':', ';', '¿', '?', '¡', '!', '"', ' '] # Signos que no afectan
    signosf = ['.', '?', '!'] # Signos que afectan
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    j = len(cadena)
    palabras = []
    cad = ""
    arr_err = []
    #   Aqui se separan las palabras que se van a analizar
    for i in range(j):
        flg = cadena[i].isspace()
        if cadena[i].islower() == True or cadena[i].isupper() == True or \
                num.__contains__(cadena[i]) == True:
            cad = cad + cadena[i].lower()
        elif cadena[i].isspace() == True and len(cad) != 0:
            palabras.append(cad)
            cad = ""
            palabras.append(cadena[i])
        elif cadena[i].isspace() == True and len(cad) == 0:
            palabras.append(cadena[i])
        elif cadena[i].islower() == False and cadena[i].isupper() == False and \
                num.__contains__(cadena[i]) == False:
            if len(cad) != 0:
                palabras.append(cad)
                cad = ""
            palabras.append(cadena[i])
    if cad != " " and len(cad) != 0:
        if cad != 0:
            palabras.append(cad)
    #   Aqui se lee el documento de las etiquetas
    doc = open("C:/Users/zetha/Desktop/TT-R-20-1-006/Diccionario_de_palabras/Etiquetado.txt", "r+",encoding="utf8")
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
            elif palabras[h] == '(':
                arr.append(2)
                break
            elif palabras[h] == ')':
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
        #k = pos
        if pos == 0:
            if arr[i] == 'A' or arr[i] == 'F':
                pos = 1
            elif arr[i] == 'B':
                pos = 2
            elif arr[i] == 'C':
                pos = 7
            elif arr[i] == 'D':
                pos = 12
            elif arr[i] == 'E':
                pos = 6
            elif arr[i] == 'G':
                pos = 11
            elif arr[i] == 'H':
                pos = 10

        elif pos == 1:
            if arr[i] == 'A' or arr[i] == 'C' or arr[i] == 'D' or arr[i] == 'E' or arr[i] == 'F' or arr[i] == 'G' \
                    or arr[i] == 'H':
                pos = -1
            elif arr[i] == 'B':
                pos = 2

        elif pos == 2:
            if arr[i] == 'A':
                pos = 1
            elif arr[i] == 'B' or arr[i] == 'E' or arr[i] == 'H':
                pos = 2
            elif arr[i] == 'C':
                pos = 3
            elif arr[i] == 'D':
                pos = 5
            elif arr[i] == 'F':
                pos = 4
            elif arr[i] == 'G':
                pos = 9

        elif pos == 3:
            if arr[i] == 'A':
                pos = 1
            elif arr[i] == 'B':
                pos = 2
            elif arr[i] == 'C':
                pos = 3
            elif arr[i] == 'D':
                pos = 5
            elif arr[i] == 'E' or arr[i] == 'F' or arr[i] == 'H':
                pos = -1
            elif arr[i] == 'G':
                pos = 9

        elif pos == 4:
            if arr[i] == 'A':
                pos = 1
            elif arr[i] == 'B':
                pos = 2
            elif arr[i] == 'C':
                pos = 3
            elif arr[i] == 'D':
                pos = 5
            elif arr[i] == 'E' or arr[i] == 'G' or arr[i] == 'H':
                pos = -1
            elif arr[i] == 'F':
                pos = 4

        elif pos == 5:
            if arr[i] == 'A':
                pos = 1
            elif arr[i] == 'B':
                pos = 2
            elif arr[i] == 'C' or arr[i] == 'E' or arr[i] == 'H':
                pos = -1
            elif arr[i] == 'D':
                pos = 5
            elif arr[i] == 'F':
                pos = 4
            elif arr[i] == 'G':
                pos = 9

        elif pos == 6:
            if arr[i] == 'A':
                pos = 1
            elif arr[i] == 'B':
                pos = 2
            elif arr[i] == 'C':
                pos = 7
            elif arr[i] == 'D' or arr[i] == 'E' or arr[i] == 'F':
                pos = -1
            elif arr[i] == 'G':
                pos = 8
            elif arr[i] == 'H':
                pos = 2

        elif pos == 7:
            if arr[i] == 'A':
                pos = 1
            elif arr[i] == 'B':
                pos = 2
            elif arr[i] == 'C':
                pos = 7
            elif arr[i] == 'D':
                pos = 4
            elif arr[i] == 'E' or arr[i] == 'F' or arr[i] == 'G':
                pos = -1
            elif arr[i] == 'H':
                pos = 10

        elif pos == 8:
            if arr[i] == 'A' or arr[i] == 'B' or arr[i] == 'D' or arr[i] == 'E' or arr[i] == 'F' or arr[i] == 'G' \
                    or arr[i] == 'H':
                pos = -1
            elif arr[i] == 'C':
                pos = 7

        elif pos == 9:
            if arr[i] == 'A' or arr[i] == 'B' or arr[i] == 'D' or arr[i] == 'E' or arr[i] == 'F' or arr[i] == 'G' \
                    or arr[i] == 'H':
                pos = -1
            elif arr[i] == 'C':
                pos = 3

        elif pos == 10:
            if arr[i] == 'A':
                pos = 1
            elif arr[i] == 'B':
                pos = 2
            elif arr[i] == 'C':
                pos = 7
            elif arr[i] == 'D' or arr[i] == 'E' or arr[i] == 'F' or arr[i] == 'H':
                pos = -1
            elif arr[i] == 'G':
                pos = 8

        elif pos == 11:
            if arr[i] == 'A' or arr[i] == 'B' or arr[i] == 'D' or arr[i] == 'E' or arr[i] == 'F' or arr[i] == 'G' \
                    or arr[i] == 'H':
                pos = -1
            elif arr[i] == 'C':
                pos = 7

        elif pos == 12:
            if arr[i] == 'A':
                pos = 1
            elif arr[i] == 'B':
                pos = 2
            elif arr[i] == 'C' or arr[i] == 'E' or arr[i] == 'F' or arr[i] == 'G' or arr[i] == 'H':
                pos = -1
            elif arr[i] == 'D':
                pos = 12

        elif pos == -1 and flg == 0:
            flg = 1
            #respuesta = "Tu error se originó en la palabra: %d" % i
            print("Tu error se originó en la palabra: %d" % i)
            arr_err.append(i)

        # Si encuentra un signo de puntuación, reinicia el autómata
        if arr[i] == 1:
            if ef.__contains__(pos) == False:
                #respuesta = "Tu estado (%d) no es un estado final, por lo que la oración está mal." % pos
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
            if ef.__contains__(pos) == False:
                ##respuesta = "Tu estado (%d) no es un estado final, por lo que la oración está mal." % pos
                print("Tu estado (%d) no es un estado final, por lo que la oración está mal." % pos)
                arr_err.append(i)
            pos = h
            h = 0
            flg = hflg
            hflg = 0
        #print("%i: %s, %i" % (k, arr[i], pos))

    if ef.__contains__(pos) == True:
        ##respuesta = "Felicidades, tu cadena se escribió con exito!"
        print("Felicidades, tu cadena se escribió con exito!")
    
    #print(palabras)
    #print(arr)
    return arr_err
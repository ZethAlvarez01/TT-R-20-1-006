def evalua_frases(cadena):
    
    j = len(cadena)
    cadena = cadena.replace(u'\xa0',' ',j)
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
        if cadena[i].islower() is True or cadena[i].isupper() is True or num.__contains__(cadena[i]) is True:
            cad = cad + cadena[i]
        elif cadena[i].isspace() is True and len(cad) != 0:
            palabras.append(cad)
            cad = ""
            palabras.append(cadena[i])
        elif cadena[i].isspace() is True and len(cad) == 0:
            palabras.append(cadena[i])
        elif cadena[i].islower() is False and cadena[i].isupper() is False and num.__contains__(cadena[i]) is False:
            if len(cad) != 0:
                palabras.append(cad)
                cad = ""
            palabras.append(cadena[i])


    if cad != " " and len(cad) != 0:
        if cad != 0:
            palabras.append(cad)  # Agrega la ultima palabra al arreglo si no es un espacio o cadena vacía

    
    print(palabras)
    
    #   Aqui se lee el documento de las etiquetas
    doc = open("Diccionario_de_palabras/Etiquetado.txt", "r+",encoding="utf8")
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
    #print(arr)

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
            if( i != 1):
                arr_err.append(i -1)
            arr_err.append(i)
            if( i != len(palabras)):
                arr_err.append(i +1)

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
                if( i != 1):
                    arr_err.append(i -1)
                arr_err.append(i)
                if( i != len(palabras)):
                    arr_err.append(i +1)
            pos = h
            h = 0
            flg = hflg
            hflg = 0
        #print("%i: %s, %i" % (k, arr[i], pos))

    if ef.__contains__(pos) == True:
        ##respuesta = "Felicidades, tu cadena se escribió con exito!"
        print("Felicidades, tu cadena se escribió con exito!")

    arr_completo = []
    cont = 0

    if(len(arr_err) != 0):
        for i in range(0,len(palabras)):
            arr_completo.append(palabras[i])
            if i == arr_err[cont]:
                arr_completo.append(False)
                cont = cont + 1
                if (cont >= len(arr_err)):
                    cont = 0
            else:
                arr_completo.append(True)
            arr_completo.append(0)
    else:
        for i in range(0,len(palabras)):
            arr_completo.append(palabras[i])
            arr_completo.append(True)
            arr_completo.append(0)
    
    
    print("Arrelo completo")
    print(arr_completo)
    print("Arrelo sdsd")
    print(arr_err)
    return arr_completo
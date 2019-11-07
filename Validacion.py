def validacion(cadena):
    tipo_error = 0 #Variableque guarda el numero de identificacion de error:
                   # 0 = Correcto
                   # 1 = Palabra con mayusculas / minusculas / numeros intercalados
                   # 2 = Primer caracter despues de un punto es minuscula
                   # 3 = Numeros
                   # 4 = Mayuscula sola dentro de la frase
    # Algoritmo para identificar errores de mayúsculas y minúsculas en las palabras.

    # Aqui metes la cadena, frase, texto que vayas a validar.
    #cadena = "Hola hola MuY mUy muY MUy mUY"
    #signos = ['(', ')', ',', '-', ':', ';', '¿', '?', '¡', '!', '"', ' ']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    # Esto es solo para que veas en la terminal tu texto
    print(cadena)
    # Contadores i, h
    i = 0
    h = 0
    n: int = 0
    j = len(cadena)  # Tamaño de la cadena de caracteres
    #flg = False  # Bandera para identificar los espacios 0 = letra, 1 = espacio
    flg2 = False  # Bandera para identificar si la palabra esta bien escrita o no
    flgptr = True  # Bandera para identificar si acaba de pasar un punto 1 = antes habia punto, 0 = no hay punto
    palabras = []  # Arreglo en donde se van a guardar las palabras cada una por separado
    cad = ""  # Variable para concatenar los caracteres que formen cada palabra
    print("La cadena tiene %d caracteres" % j)

    # Esto solo separa la cadena por palabras poniendo los signos de puntuacion por separado
    for i in range(j):
        #flg = cadena[i].isspace()
        if cadena[i].islower() is True or cadena[i].isupper() is True or cadena[i] == '.' or num.__contains__(cadena[i]) is True:
            cad = cad + cadena[i]
        elif cadena[i].isspace() is True and len(cad) != 0:
            palabras.append(cad)
            cad = ""
            palabras.append(cadena[i])
        elif cadena[i].isspace() is True and len(cad) == 0:
            palabras.append(cadena[i])
        elif cadena[i].islower() is False and cadena[i].isupper() is False and cadena[i] != '.' and num.__contains__(cadena[i]) is False:
            if len(cad) != 0:
                palabras.append(cad)
                cad = ""
            palabras.append(cadena[i])
    if cad != " " and len(cad) != 0:
        if cad != 0:
            palabras.append(cad)  # Agrega la ultima palabra al arreglo si no es un espacio o cadena vacía

    print(palabras)  # se imprimen las palabras 

    npal = palabras.__len__()  # Número de palabras encontradas

    # Aqui se checa que esten bien escritas palabra por palabra
    i = 0
    lista = list()
    for i in range(npal):
        h = 0
        p = 0
        r = 0
        s = 0
        n = len(palabras[i]) - 1
        if i > 0:
            n1 = len(palabras[i-2]) - 1
            k = 0
            while k < len(palabras[i-2]):  # cuenta cuantos puntos tiene la palabra anterior
                if palabras[i-2].__getitem__(k) == '.':
                    p += 1
                k += 1

        flg2 = True
        tipo_error = 0
        #print(p)
        while h < len(palabras[i]):
            if i > 1 and p == 1 and palabras[i - 2].__getitem__(n1) == '.':  # Indica si la palabra anterior tenía un punto
                flgptr = True
                #print("Bandera activa")
            if i > 1 and palabras[i - 2].__getitem__(n1) != '.':  # Indica si la palabra anterior no tenía un punto
                flgptr = False
                #print("Bandera inactiva")
            if i == 0:  # Indica que al inicio de la cadena debe haber una mayuscula
                flgptr = True
                #print("Bandera activa")
            if i > 1 and p > 1:
                flgptr = False



            # manda error si es minuscula despues del punto
            if palabras[i].__getitem__(0).islower() is True and flgptr is True:
                flg2 = False
                tipo_error = 2
                break

            # error si hay mayusculas entre la frase
            if len(palabras[i]) == 1 and palabras[i].isupper() is True and flgptr is False:
                flg2 = False
                tipo_error = 4
                break

            # si la palabra empieza con mayuscula y tiene mezcla de minúsculas o números
            if palabras[i].__getitem__(0).isupper() is True and n > 0:
                if h > 0 and palabras[i].__getitem__(h).isupper() is True and r == 0:
                    r = 1
                if h > 0 and palabras[i].__getitem__(h).islower() is True and r > 0:
                    flg2 = False
                    tipo_error = 1
                    break
                if h > 0 and palabras[i].__getitem__(h).isupper() is True and \
                        palabras[i].__getitem__(h-1).islower() is True:
                    flg2 = False
                    tipo_error = 1
                    break
                if h > 0 and palabras[i].__getitem__(h).isupper() is False and palabras[i].__getitem__(h).islower() is \
                        False and palabras[i].__getitem__(h) != '.':
                    flg2 = False
                    tipo_error = 1
                    break

            # checa si la palabra empieza con minusculas y tiene mayusculas o numeros
            if palabras[i].__getitem__(0).islower() is True and n > 0:
                if h > 0 and palabras[i].__getitem__(h).islower() is True and s == 0:
                    s += 1
                if h > 0 and palabras[i].__getitem__(h).isupper() is True:
                    flg2 = False
                    tipo_error = 1
                    break
                if h > 0 and palabras[i].__getitem__(h).isupper() is False and palabras[i].__getitem__(h).islower() is \
                        False and palabras[i].__getitem__(h) != '.':
                    flg2 = False
                    tipo_error = 1
                    break

            # Verifica que solo sean números o un numero con decimales
            if palabras[i].__getitem__(0).isdigit() is True and n > 0:
                if palabras[i].isdigit() is False or palabras[i].isdecimal() is False:
                    flg2 = False
                    tipo_error = 3
                    break

            h += 1
        # Se imprime la palabra, True = valido, False = rechazado
        print("Palabra %d: %s ==> %s" % (i + 1, palabras[i], flg2))
        lista.append(palabras[i])
        lista.append(flg2)
        lista.append(tipo_error)
        tipo_error = 0

    return lista
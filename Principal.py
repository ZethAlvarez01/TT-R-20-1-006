# Algoritmo para identificar errores de mayúsculas y minúsculas en las palabras.
def validacion(cadena):
    tipo_error = 0 #Variableque guarda el numero de identificacion de error:
                   # 0 = Correcto
                   # 1 = Palabra con mayusculas o minusculas intercaladas
                   # 2 = Primer caracter despues de un punto es minuscula
                   # 3 = Si mayusculas sueltas
    print(cadena)
# Contadores i, h
    i = 0
    h = 0
    n = 0
    j = len(cadena)  # Tamaño de la cadena de caracteres
    flg = False  # Bandera para identificar los espacios 0 = letra, 1 = espacio
    flg2 = False  # Bandera para identificar si la palabra esta bien escrita o no
    flgptr = True  # Bandera para identificar si acaba de pasar un punto 1 = antes habia punto, 0 = no hay punto
    palabras = []  # Arreglo en donde se van a guardar las palabras cada una por separado
    cad = ""  # Variable para concatenar los caracteres que formen cada palabra
    print("La cadena tiene %d caracteres" % j)

    for i in range(j):  # Ciclo para separar palabra por palabra
        flg = cadena[i].isspace()
        if flg is True and cad != "":
            palabras.append(cad)
            cad = ""
        # Si es un caracter, lo concatena con los demas caracteres en cad
        else:
            if cadena[i] != " ":
                cad = cad + cadena[i]
    if cad != " " and cad != "":
        if cad != 0:
            palabras.append(cad)  # Agrega la ultima palabra al arreglo si no es un espacio o cadena vacía

    print(palabras)
    npal = palabras.__len__()  # Número de palabras encontradas
    i = 0
    lista = list()
    for i in range(npal):  # Ciclo para checar palabra por palabra.
        h = 0
        if i > 0:
            n = len(palabras[i-1]) - 1
        flg2 = True
        
        while h < len(palabras[i]):

            if palabras[i-1].__getitem__(n) is '.':  # Indica si la palabra anterior tenía un punto
                flgptr = True
            if palabras[i-1].__getitem__(n) != '.':  # Indica si la palabra anterior no tenía un punto
                flgptr = False
            if i == 0:  # Indica que al inicio de la cadena debe haber una mayuscula
                flgptr = True

            if palabras[i].islower() is True and flgptr is True:  # manda error si es minuscula despues del punto
                flg2 = False
                tipo_error = 2
                break

            if len(palabras[i]) == 1 and palabras[i].isupper() is True and flgptr is False:  # error si mayusculas sueltas
                flg2 = False
                tipo_error = 3
                break

            # Verifica si el primer caracter tiene que ser mayuscula dependiendo de la bandera de punto
            if (h == 0) and (flgptr is True):
                flg2 = palabras[i].__getitem__(h).isupper()
                if(flg2 is True):
                    tipo_error = 0
                else:
                    tipo_error = 2
                break

            if palabras[i].islower() is False and palabras[i].isupper() is False:  # Manda error si hay mayusculas y minusculas
                if h > 0 and palabras[i].__getitem__(h).islower() is False:
                    flg2 = False
                    tipo_error = 1
                    break

            h += 1
        # Se imprime la palabra, True = valido, False = rechazado
        print("Palabra %d: %s ==> %s" % (i + 1, palabras[i], flg2))
        lista.append(palabras[i])
        lista.append(flg2)
        lista.append(tipo_error)
        tipo_error = 0
        
        
    return lista

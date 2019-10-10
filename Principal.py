# Algoritmo para identificar errores de mayúsculas y minúsculas en las palabras.
def validacion(cadena):
    # Aqui metes la cadena, frase, texto que vayas a validar.
    # Esto es solo para que veas en la terminal tu texto
    print(cadena)
    # Contadores i, h
    i = 0
    h = 0
    j = len(cadena)  # Tamaño de la cadena de caracteres
    flg = False  # Bandera para identificar los espacios 0 = letra, 1 = espacio
    flg2 = False  # Bandera para identificar si la palabra esta bien escrita o no
    flgptr = True  # Bandera para identificar si acaba de pasar un punto 1 = antes habia punto, 0 = no hay punto
    palabras = []  # Arreglo en donde se van a guardar las palabras cada una por separado
    cad = ""  # Variable para concatenar los caracteres que formen cada palabra
    print("La cadena tiene %d caracteres" % j)


    for i in range(j):  # Ciclo para separar palabra por palabra
        # Bandera identificadora de espacios
        flg = cadena[i].isspace()
        # Si hay un espacio, guarda los caracteres concatenados como una palabra
        if flg is True and cad != "":
            palabras.append(cad)  # Agrega cada palabra al arreglo
            cad = ""
        # Si es un caracter, lo concatena con los demas caracteres en cad
        else:
            if cadena[i] != " ":  # Valida que no haya espacios juntos
                cad = cad + cadena[i]
    if cad != " " and cad != "":
        palabras.append(cad)  # Agrega la ultima palabra al arreglo si no es un espacio o cadena vacía


    print(palabras)
    npal = palabras.__len__()  # Número de palabras encontradas
    i = 0
    lista=list()
    for i in range(npal):  # Ciclo para checar palabra por palabra.
        h = 0
        flg2 = True
        # While que recorre caracter por caracter cada palabra
        while h < len(palabras[i]):
            # Valida si toda la palabra está en mayusculas
            if len(palabras[i]) > 1 and palabras[i].isupper() is True:
                flg2 = True
                break
            # Valida que las palabras de un caracter dentro de la frase sean con minúsculas
            if len(palabras[i]) == 1 and palabras[i].islower() is True and flgptr is False:
                flg2 = True
                break
            # Valida que las palabras de un caracter dentro de la frase no sean con mayusculas
            if len(palabras[i]) == 1 and palabras[i].isupper() is True and flgptr is False:
                flg2 = False
                break
            # Verifica si el primer caracter tiene que ser mayuscula dependiendo de la bandera de punto
            if (h == 0) and (flgptr is True):
                flg2 = palabras[i].__getitem__(h).isupper()
                flgptr = False
            # Indica si es mayuscula o no desde el segundo caracter
            if (h >= 1) and (h < len(palabras[i])) and (palabras[i].__getitem__(h).isupper()) is True:
                flg2 = False
            # Indica si la palabra anterior tenía un punto al final
            if (h == len(palabras[i]) - 1) and palabras[i].__getitem__(h) == '.':
                flgptr = True
                # print("Latra %d: %s ===> %s" % (h + 1, palabras[i].__getitem__(h), flg2))
            h += 1
        # Se imprime la palabra, True = valido, False = rechazado
        print("Palabra %d: %s ==> %s" % (i + 1, palabras[i], flg2))
        lista.append(palabras[i])
        lista.append(flg2)
        
        
    return lista

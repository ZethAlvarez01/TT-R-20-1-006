def sin_acentos(texto):

    vocales_a = ["á","é","í","ó","ú"]
    vocales_s = ["a","e","i","o","u"]

    flg = 0
    cad =""
    for i in range(0, len(texto)):
        flg = 0
        for j in range(0, len(vocales_a)):
            if( texto[i] == vocales_a[j] ): 
                cad = cad + vocales_s[j]
                flg = 1
        if(flg == 0):
            cad = cad + texto[i]
    
    return cad

def buscar_sug(texto):

    longitud = len(texto)
    longitud_arch = 0

    ini = texto[0]

    arreglo_2 = [" "," "] 

    try:
        archivo = open("Diccionario_de_palabras/PorInicialyTamano/"+ini+str(longitud)+".txt","r+",encoding="utf8")
        
        tamaño_palabras_d = 0
        palabras = []
        cad = ""     
        for linea in archivo.readlines():
            tamaño_palabras_d = tamaño_palabras_d + 1
            cad = ""
            for i in range(0,len(linea) -1):
                cad = cad + linea[i]
            palabras.append(cad)
        tamaño_palabras_d = tamaño_palabras_d - 1
        pivote = int(tamaño_palabras_d / 2)

        longitud_arch = len(palabras) - 1
        
        min = 0
        max = len(palabras)

        busco = sin_acentos(texto).lower()
        comparo = sin_acentos(palabras[pivote]).lower()
        aux = 0
        ant = ""
        print(comparo)

        while( aux < longitud):
            if(busco[aux] == comparo[aux]):
                print("Igual")
                ant = busco[aux]
                aux = aux + 1
                if aux == longitud:
                    break
            if(busco[aux] < comparo[aux]):
                print("Arriba")
                max = pivote
                pivote = pivote - int((pivote - min) / 2)
                comparo = sin_acentos(palabras[pivote]).lower()
                print(comparo)
                if( ant != comparo[aux-1]):
                    while ant != comparo[aux-1]:
                        pivote = pivote + 1
                        comparo = sin_acentos(palabras[pivote]).lower()
                if (pivote == max):
                    break
            if(busco[aux] > comparo[aux]):
                print("Abajo")
                min = pivote
                pivote = pivote + int((max - pivote) / 2)
                comparo = sin_acentos(palabras[pivote]).lower()
                print(comparo)

                if( ant != comparo[aux-1]):
                    while ant != comparo[aux-1]:
                        pivote = pivote - 1
                        comparo = sin_acentos(palabras[pivote]).lower()
                if (pivote == min):
                    break
        

        print("------")
        print(busco)
        print(comparo)
        print(palabras[pivote])
        
        arreglo_2[0] = palabras[pivote]
        if( pivote + 1 < longitud_arch - 1): 
            arreglo_2[1] = palabras[pivote + 1]
        else:
            arreglo_2[1] = palabras[pivote - 1]

        print(arreglo_2)
        return arreglo_2

    except IOError:
        arr_err = [" ", " "]
        return arr_err
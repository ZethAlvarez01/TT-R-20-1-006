def buscar_sug(texto):
    longitud = len(texto)
    ini = texto[0]
    vocales_a = ["á","é","í","ó","ú"]
    vocales_s = ["a","e","i","o","u"]
    arreglo_2 = [" "," "] 

    try:
        archivo = open("Diccionario_de_palabras/PorInicialyTamano/"+ini+str(longitud)+".txt","r+",encoding="utf8")
        
        tam = 0
        palabras = []
        cad = ""     

        for linea in archivo.readlines():
            tam = tam + 1
            cad = ""
            for i in range(0,len(linea) -1):
                cad = cad + linea[i]
            palabras.append(cad)

        tam = tam - 1
        pivote = int(tam / 2)


        palabra = palabras[pivote]
        for i in range(0, len(palabra)):
            for j in range(0, len(vocales_a)):
                if( palabra[i] == vocales_a[j] ): 
                    palabra[i] = vocales_s[j]
        



        return arreglo_2

    except IOError:
        arr_err = [" ", " "]
        return arr_err


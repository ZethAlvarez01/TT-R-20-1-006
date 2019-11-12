def buscar_sug(texto):
    longitud = len(texto)
    ini = texto[0]

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

        print("Mitad: "+palabra+" "+texto)

        aux = 0
        max = longitud
        min = 0


        while aux < longitud:
            if(texto[aux] == palabra[aux]):
                aux = aux + 1
            else:
                if(palabra[aux] < texto[aux]):
                    print(palabra[aux] + "<" + texto[aux])
                    #Arriba
                    max = pivote
                    pivote = pivote - int(((pivote - min) / 2))
                    if palabra == palabras[pivote]:
                        break
                    else:
                        palabra = palabras[pivote]
                    print(palabra)
                else:
                    print(palabra[aux] + "<" + texto[aux])
                    #Abajo
                    min = pivote
                    pivote = pivote + int(((max - pivote) / 2))
                    if palabra == palabras[pivote]:
                        break
                    else:
                        palabra = palabras[pivote]
                    print(palabra)
                    
                    

        print("Sigerencia: "+palabra)

        return arreglo_2

    except IOError:
        arr_err = [" ", " "]
        return arr_err


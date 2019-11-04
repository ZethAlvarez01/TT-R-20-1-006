archivo = open("Diccionario_palabras.txt","r+")
i = 0

for linea in archivo.readlines():
	tamano = len(linea) - 1
	caracter = linea[0]
	archivoN = open("C:/Users/zetok/Desktop/TT-R-20-1-006/Diccionario_de_palabras/PorInicialyTamano/"+caracter+str(tamano)+".txt","a+")
	archivoN.write(linea)
	archivoN.close()
	i = i + 1
	print("Cargando... "+str(i)+" %")

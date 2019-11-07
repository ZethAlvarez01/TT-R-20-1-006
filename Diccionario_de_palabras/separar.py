archivo = open("Diccionario_palabras.txt","r+",encoding="utf8")
i = 0

for linea in archivo.readlines():
	tamano = len(linea) - 1
	caracter = linea[0].lower()
	archivoN = open("C:/Users/zetok/Desktop/TT-R-20-1-006/Diccionario_de_palabras/PorInicialyTamano/"+caracter+str(tamano)+".txt","a+",encoding="utf8")
	archivoN.write(linea)
	archivoN.close()
	i = i + 1
	print("Cargando... "+str(i)+" %")

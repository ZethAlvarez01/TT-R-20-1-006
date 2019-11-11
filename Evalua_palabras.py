def buscar(palabra):
		
	aux = []
	long = len(palabra)

	ini = palabra[0]

	try:
		archivo = open("Diccionario_de_palabras/PorInicialyTamano/"+ini+str(long)+".txt","r+",encoding="utf8")
		#print("Si entro")

		for linea in archivo.readlines():
			#print(str(len(linea))+ " " + str(long))
			auxP = ""
			longi = len(linea) - 1
			for i in range(0,longi):
				auxP = auxP + linea[i]
			#print(str(len(auxP))+ " " + str(long))
			aux.append(auxP)

		for pal in aux:
			if ( pal ==  palabra):
				return 1
		return 0

	except IOError:
		return 0

	
def evalua_palabra(cadena):
	cadena = cadena.replace(u'\xa0', u' ')
	#print("Cad: recibida: "+cadena)
	j = len(cadena)
	cad = ""
	palabras = []
	num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	conti = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0','(', ')', ',', '-', '.', ':', ';', '¿', '?', '¡', '!', '"'," "]
	arr_err = []

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
				cad=""
			palabras.append(cadena[i])

	#print(palabras)

	if cad != " " and len(cad) != 0:
		if cad != 0:
			palabras.append(cad)
			
	for palabra in palabras:
		arr_err.append(palabra)

		flg = 0
		for i in conti:
			if ( i in palabra ) == True:
				flg = 1
		if (flg == 1):
			arr_err.append(2) # Incorrecta 0 Correcta 1 no apta a buscar 2
			arr_err.append(404)
		else:	
			tipo = 0
			tipo2 = 0
			if(palabra.islower() == True):
				tipo = buscar(palabra)
			elif(palabra.isupper() == True):
				tipo = buscar(palabra.lower())
			elif(palabra[0].isupper() == True):
				tipo = buscar(palabra)
				tipo2 = buscar(palabra.lower())
				if(tipo >= tipo2):
					tipo = tipo
				else:
					tipo = tipo2

			arr_err.append(tipo)
			arr_err.append(404)
	
	return arr_err









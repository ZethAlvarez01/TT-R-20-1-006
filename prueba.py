cadena = "holaz como estás?"
j = len(cadena)
cad = ""
palabras = []
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
com = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0','(', ')', ',', '-', '.', ':', ';', '¿', '?', '¡', '!', '"'," "]
arr_err = []

def buscar(palabra):
	aux = []
	long = len(palabra)
	ini = palabra[0]
	
	archivo = open("C:/Users/zetok/Desktop/TT-R-20-1-006/Diccionario_de_palabras/PorInicialyTamano/"+ini+str(long)+".txt","r+")
	for linea in archivo.readlines():
		aux2 = linea.split()
		linea = aux2[0]
		aux.append(linea)
	for pal in aux:
		if ( pal ==  palabra):
			return 3
	return 1

for i in range(j):
	if cadena[i].islower() is True or cadena[i].isupper() is True or cadena[i] == '.' or \
		num.__contains__(cadena[i]) is True:
			cad = cad + cadena[i]
	elif cadena[i].isspace() is True and len(cad) != 0:
		palabras.append(cad)
		cad = ""
		palabras.append(cadena[i])
	elif cadena[i].isspace() is True and len(cad) == 0:
		palabras.append(cadena[i])
	elif cadena[i].islower() is False and cadena[i].isupper() is False and cadena[i] != '.' and \
			num.__contains__(cadena[i]) is False:
		if len(cad) != 0:
			palabras.append(cad)
			cad = ""
			palabras.append(cadena[i])

if cad != " " and len(cad) != 0:
	if cad != 0:
		palabras.append(cad) 
	    

print(palabras) 


for palabra in palabras:
	arr_err.append(palabra)
	flg = 0
	for i in com:
		if ( i in palabra ) == True:
			flg=1
	if (flg == 1):
		arr_err.append(1)
		arr_err.append(4)
	else:	
		arr_err.append(0)
		arr_err.append(buscar(palabra))

print(arr_err)









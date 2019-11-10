
archivo2 = open("PalabrasS.txt","r+",encoding="utf8")

cont2 = 0

for i in archivo2.readlines():
	print(cont2)
	cont2 = cont2 + 1
	ini = i[0]
	long = len(i)-1
	archivo = open("PorInicialyTamano/"+ini+str(long)+".txt","r+",encoding="utf8")

	for linea in archivo.readlines():
		if ( i ==  linea):
			archivo3 = open("PalabrasS2.txt","a+",encoding="utf8")
			archivo3.write(i)
			archivo3.close()
		archivo4 = open("PorInicialyTamano/"+ini+str(long)+".txt","a+",encoding="utf8")
		archivo4.write("")
		archivo4.close()
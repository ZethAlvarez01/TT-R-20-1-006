
archivo2 = open("PalabrasS.txt","r+",encoding="utf8")

cont2 = 0
cont3 = 0

for i in archivo2.readlines():
	
	cont2 = cont2 + 1
	ini = i[0]
	long = len(i)-1

	archivo4 = open("PorInicialyTamano/"+ini+str(long)+".txt","a+",encoding="utf8")
	archivo4.write(" ")
	archivo4.close()

	archivo = open("PorInicialyTamano/"+ini+str(long)+".txt","r+",encoding="utf8")
	flg = 0
	for linea in archivo.readlines():
		if ( i ==  linea):
			flg = 1
	if( flg == 0 ):
		cont3 = cont3 +1
		archivo3 = open("Excluidas.txt","a+",encoding="utf8")
		archivo3.write(i)
		archivo3.close()

print(cont2)
print(cont3)


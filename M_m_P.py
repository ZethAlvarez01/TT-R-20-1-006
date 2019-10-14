
cadena="hola esTo es una a A ver que 2  PaSA PRUEBA. esto sigue siendo una. Prueba. . ."
i = 0
l_cad = len(cadena)
flg = True
cad=""
palabras = []

def switch(caracter,estado):
    if(estado==0):
        if(caracter.isupper() is True):
            estado = 1
        else:
            estado = 6
    elif(estado == 1):
        if(caracter.isupper() is True):
            estado = 2
        elif(caracter.islower() is True):
            estado = 3
        elif(caracter.isspace() is True):
            estado = 4
        else:
            estado = 7
    elif(estado==2):
        if(caracter.isupper() is True):
            estado = 2
        elif(caracter.isspace() is True):
            estado = 4
        elif(caracter == "."):
            estado = 5
        else:
            estado = 8
    elif(estado==3):
        if(caracter.islower() is True):
            estado = 3
        elif(caracter.isspace() is True):
            estado = 4
        elif(caracter == "."):
            estado = 5
        else:
            estado = 8
    elif(estado==4):
        if(caracter.isupper() is True):
            estado = 1
        elif(caracter.islower() is True):
            estado = 1
        else:
            estado = 9
    elif(estado==5):
        if(caracter.isspace() is True):
            estado = 0
        else:
            estado = 9
    else:
        return 10
    return estado

estado = 0
j=l_cad
espacio=False

for i in range(j):  # Ciclo para separar palabra por palabra
    flg = cadena[i].isspace()
    if flg is True and cad != "":
        palabras.append(cad)
        cad = ""
    # Si es un caracter, lo concatena con los demas caracteres en cad
    else:
        if cadena[i] != " ":
            cad = cad + cadena[i]
if cad != " " and cad != "":
    if cad != 0:
        palabras.append(cad)  # Agrega la ultima palabra al arreglo si no es un espacio o cadena vacía

print(palabras)
npal = palabras.__len__()  # Número de palabras encontradas
i = 0
ix = 0

validado = list()

while(i < l_cad):
    estado = switch(cadena[i],estado)
    print(cadena[i],estado)
    if estado == 4:
        ix+=1
    if(estado > 5):
        print("error")
        estado = 4
    i+=1


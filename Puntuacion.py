# Algoritmo para identificar errores de puntuación: paréntesis, comas, guiones, puntos,
# doble punto, punto y coma, interrogación, exclamación y comillas dobles
def error_signos(cadena):
    #cadena = "Intentemos probar esto (esto es una prueba) ( hj."
    signos = ['(', ')', ',', '-', '.', ':', ';', '¿', '?', '¡', '!', '"']  # Arreglo de signos a validar
    signos1 = ['(', ')', '-', ':', ';', '¿', '?', '¡', '!', '"']  # Arreglo de signos a validar
    signos2 = [',', '.', ':', ';']  # Arreglo de signos sin interrogacion, exclamacion , parentesis y doble comilla
    signos3 = ['(', ',', '-', ':', '¿', '?', '¡', '!', '"']  # Arreglo de signos a validar despues de cerrar comillas
    signos4 = [')', ',', '-', ':', ';', '¿', '?', '¡', '!', '"']  # Signos para comparar domillas dobles
    signos5 = [',', '-', ':', ';', '"']  # Signos para comparar domillas dobles
    signos6 = [',', '-', ':', ';', '.', ')', '(']  # Signos para comparar parentesis
    signos7 = ['?', '¿', '!', '¡', '(', ')', '"']  # Signos para validación de apertura
    pilac = []
    pilan = []
    aerr = []  # 1 = '.', 2 = ',', 3 = '-', 4 = ':', 5 = ';', 6 = '"' y 7 = '(' ')' '¿' '?' '¡' '!'
    i = 0  # contador 1
    j = len(cadena)  # contador de caracteres de cadena

    auxcda: int = 0  # Auxiliar para comillas dobles


    for i in range(j):

        #   Aqui se manejan las reglas para el punto .********************************************

        if cadena[i] is '.':
            if i > 0 and cadena[i - 1].isspace() is True:  # Si el punto está después de un espacio
                print("Caracter: %d: no puede haber espacio antes del punto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(1)
            if 0 < i < j - 1 and cadena[
                i + 1].islower() is True:  # Si el punto está antes de una letra minuscula
                print("Caracter: %d: no puede llevar un caracter minúscula despues del punto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(1)
            if 0 < i < j - 1 and (cadena[i + 1].islower() is True and cadena[
                i + 2].islower() is True):  # Si hay una palabra despues del punto
                print("Caracter: %d: no puede llevar una palabra despues del punto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(1)
            if i < j - 4 and cadena[i + 1] == cadena[i + 2] == cadena[i + 3] == '.':
                print("Caracter: %d: solo se utilizan 3 puntos para puntos suspensivos." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(1)
            if i > 1 and (cadena[i - 1] == ':' or cadena[i - 1] == ';'):
                print("Caracter: %d: no se puede poner un punto despues de un doble punto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(1)

        #   Aqui se manejan las reglas para la coma ,********************************************

        if cadena[i] is ',':
            if i < j - 1 and cadena[i + 1].isspace() is False:
                print("Caracter: %d: no se puede poner una coma antes de otro caracter." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(2)
            if i > 0 and signos2.__contains__(cadena[i - 1]) is True:
                print("Caracter: %d: no se puede poner una coma despues de un signo de puntuación." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(2)
            if i == 0:
                print("Caracter: %d: no se puede iniciar una frase con una coma." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(2)
            if i > 0 and cadena[i - 1].isspace() is True:
                print("Caracter: %d: no puede llevar espacio antes de la coma." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(2)
            if i < j - 1 and (cadena[i + 1].islower() is True or cadena[i + 1].isupper() is True):
                print("Caracter: %d: no puede llevar un caracter despues de la coma." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(2)

        #   Aqui se manejan las reglas para el guion -********************************************

        if cadena[i] is '-':
            if i < j - 1 and signos1.__contains__(cadena[i + 1]) is True:
                print("Caracter: %d: el guion no puede ir seguido de otro signo." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(3)
            if i > 0 and signos.__contains__(cadena[i - 1]) is True:
                print("Caracter: %d: el guion no puede ir despues de otro signo." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(3)
            if i == j - 1:
                print("Caracter: %d: el guión no puede ir al final del texto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(3)

        #   Aqui se manejan las reglas para el doble punto :********************************************

        if cadena[i] is ':':
            if i < j - 1 and signos.__contains__(cadena[i + 1]) is True:
                print("Caracter: %d: el doble punto no puede ir seguido de otro signo." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(4)
            if i > 0 and (
                    cadena[i - 1].isupper() is False and cadena[i - 1].islower() is False and cadena[i - 1] != '.'):
                print("Caracter: %d: caracter no valido antes del doble punto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(4)

        #   Aqui se manejan las reglas para el punto y coma ;********************************************

        if cadena[i] is ';':
            if i == 0:
                print("Caracter: %d: el punto y coma no puede ir al inicio de una oración." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(5)
            if i > 0 and cadena[i - 1].isspace() is True:
                print("Caracter: %d: el punto y coma no puede ir después de un espacio." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(5)
            if i == j - 1:
                print("Caracter: %d: el punto y coma no puede ir al final del texto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(5)

        #   Aqui se manejan las reglas para las comillas dobles " "********************************************

        if cadena[i] is '"':

            if auxcda == 0:  # Doble comilla abierta
                auxcda = i

            if auxcda != 0 and auxcda != i:  # Doble comilla cerrada
                auxcda = 0

            if auxcda == i and 0 < i and (signos4.__contains__(cadena[i - 1]) is  # Antes de abrir "
                                        True or cadena[i - 1].isalpha() is True
                                        or cadena[i - 1].isupper() is True or
                                        cadena[i - 1].islower() is True):
                print("Caracter: %d: la doble comilla no puede ir despues de %s." % (i, cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(6)

            if auxcda == i and 0 < i and signos5.__contains__(cadena[i + 1]) is True:  # Despues de abrir "
                print("Caracter: %d: la doble comilla no puede ir antes de %s." % (i, cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(6)

            if auxcda == 0 and i < j - 1 and (signos3.__contains__(cadena[i + 1]) is  # Despues de cerrar "
                                            True or cadena[i + 1].isalpha() is True
                                            or cadena[i + 1].isupper() is True or
                                            cadena[i + 1].islower() is True):
                print("Caracter: %d: la doble comilla no puede ir antes de %s." % (i, cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(6)

            if auxcda == 0 and i < j - 1 and signos5.__contains__(cadena[i - 1]) is True:  # Antes de cerrar "
                print("Caracter: %d: la doble comilla no puede ir despues de %s." % (i, cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(6)

        if auxcda != 0 and i == j - 1:  # Se muestra la posicion en caso de que las comillas dobles no se hayan cerrado
            print("Caracter: %d: la doble comilla no se cerró." % auxcda)
            aerr.append(cadena[auxcda])
            aerr.append(auxcda)
            aerr.append(6)

        #   Aqui se manejan las reglas para ( ) ¿ ? y ¡ !********************************************

        if cadena[i] is '(' or cadena[i] is '¿' or cadena[i] is '¡':

            if 0 < i and (signos4.__contains__(cadena[i - 1]) is  # Antes de abrir (
                        True or cadena[i - 1].isalpha() is True
                        or cadena[i - 1].isupper() is True or
                        cadena[i - 1].islower() is True):
                print("Caracter: %d: el signo %s no puede ir despues de %s." % (i, cadena[i], cadena[i - 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(7)

            if 0 < i and signos6.__contains__(cadena[i + 1]) is True:  # Despues de abrir (
                print("Caracter: %d: el signo %s no puede ir antes de %s." % (i, cadena[i], cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(7)

        if cadena[i] is ')' or cadena[i] is '?' or cadena[i] is '!':

            if i < j - 1 and signos6.__contains__(cadena[i - 1]) is True:  # Antes de cerrar "
                print("Caracter: %d: el signo %s no puede ir despues de %s." % (i, cadena[i], cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(7)

            if i < j - 1 and (signos3.__contains__(cadena[i + 1]) is  # Despues de cerrar "
                            True or cadena[i + 1].isalpha() is True
                            or cadena[i + 1].isupper() is True or
                            cadena[i + 1].islower() is True):
                print("Caracter: %d: el signo %s no puede ir antes de %s." % (i, cadena[i], cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(7)

        if signos7.__contains__(cadena[i]) is True:  # Para verificar que se abra y cierre correctamente cada signo

            if len(pilac) >= 1:
                if pilac[len(pilac) - 1] is '(' and cadena[i] is ')':
                    pilac.pop()
                    pilan.pop()

                elif pilac[len(pilac) - 1] is '¡' and cadena[i] is '!':
                    pilac.pop()
                    pilan.pop()

                elif pilac[len(pilac) - 1] is '¿' and cadena[i] is '?':
                    pilac.pop()
                    pilan.pop()

                else:
                    pilac.append(cadena[i])
                    pilan.append(i)

            elif len(pilac) == 0:
                pilac.append(cadena[i])
                pilan.append(i)

    i = 0
    if len(pilac) > 0:
        for i in range(len(pilac)):
            if pilac[i] == '¿' or pilac[i] == '¡' or pilac[i] == '(' or pilac[i] == '"':
                print("En la posición %d el signo %s no se cerró" % (pilan[i], pilac[i]))
                aerr.append(pilac[i])
                aerr.append(pilan[i])
                aerr.append(8)
            if pilac[i] == '?' or pilac[i] == '!' or pilac[i] == ')':
                print("En la posición %d el signo %s se usó sin abrir" % (pilan[i], pilac[i]))
                aerr.append(pilac[i])
                aerr.append(pilan[i])
                aerr.append(8)

    print(aerr)
    return aerr
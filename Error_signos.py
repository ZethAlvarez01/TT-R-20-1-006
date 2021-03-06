# Algoritmo para identificar errores de puntuación: paréntesis, comas, guiones, puntos,
# doble punto, punto y coma, interrogación, exclamación y comillas dobles
def error_signos(cadena):
    
    # Algoritmo para identificar errores de puntuación: paréntesis, comas, guiones, puntos,
    # doble punto, punto y coma, interrogación, exclamación y comillas dobles

    #cadena = "Hola coMo estas? (\"Hola helado ) \" \""
    print(cadena)
    signos = ['(', ')', ',', '-', '.', ':', ';', '¿', '?', '¡', '!', '"']  # Arreglo de signos a validar
    signos1 = ['(', ')', '-', ':', ';', '¿', '?', '¡', '!', '"']  # Arreglo de signos a validar
    signos2 = [',', '.', ':', ';']  # Arreglo de signos sin interrogacion, exclamacion , parentesis y doble comilla
    signos3 = ['(', '-', ':', '¿', '?', '¡', '!', '"']  # Arreglo de signos a validar despues de cerrar comillas
    signos4 = [')', ',', '-', ':', ';', '¿', '?', '¡', '!', '"']  # Signos para comparar domillas dobles
    signos5 = [',', '-', ':', ';', '"']  # Signos para comparar domillas dobles
    signos6 = [',', '-', ':', ';', '.', ')', '(']  # Signos para comparar parentesis
    signos7 = ['?', '¿', '!', '¡', '(', ')', '"']  # Signos para validación de apertura
    pilac = []  # Pila para guardar los signos que tienen que cerrarse
    pilan = []  # Pila para guardar la posición de los signos que tienen que cerrarse
    aerr = []  # 1 = '.', 2 = ',', 3 = '-', 4 = ':', 5 = ';', 6 = '"' y 7 = '(' ')' '¿' '?' '¡' '!', 8 = error de apertura
    piladc = []
    i = 0  # contador 1
    j = len(cadena)  # contador de caracteres de cadena

    #auxcda: int = 0  # Auxiliar para comillas dobles

    for i in range(j):

        #   Aqui se manejan las reglas para el punto .********************************************

        if cadena[i] == '.':
            if i > 0 and cadena[i - 1].isspace() == True:  # Si el punto está después de un espacio
                print("Caracter: %d: no puede haber espacio antes del punto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(1)
            if 0 < i < j - 1 and cadena[
                i + 1].islower() == True:  # Si el punto está antes de una letra minuscula
                print("Caracter: %d: no puede llevar un caracter minúscula despues del punto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(1)
            if 0 < i < j - 1 and (cadena[i + 1].islower() == True and cadena[
                i + 2].islower() == True):  # Si hay una palabra despues del punto
                print("Caracter: %d: no puede llevar una palabra despues del punto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(1)
            if i < j - 4 and cadena[i + 1] == cadena[i + 2] == '.' and cadena[i + 3].isspace() is False:
                print("Caracter: %d: solo se utilizan 3 puntos para puntos suspensivos." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(1)
                i += 2
            if i > 1 and (cadena[i - 1] == ':' or cadena[i - 1] == ';'):
                print("Caracter: %d: no se puede poner un punto despues de un doble punto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(1)

        #   Aqui se manejan las reglas para la coma ,********************************************

        if cadena[i] == ',':
            if i < j - 1 and cadena[i + 1].isspace() == False:
                print("Caracter: %d: no se puede poner una coma antes de otro caracter." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(2)
            if i > 0 and signos2.__contains__(cadena[i - 1]) == True:
                print("Caracter: %d: no se puede poner una coma despues de un signo de puntuación." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(2)
            if i == 0:
                print("Caracter: %d: no se puede iniciar una frase con una coma." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(2)
            if i > 0 and cadena[i - 1].isspace() == True:
                print("Caracter: %d: no puede llevar espacio antes de la coma." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(2)
            if i < j - 1 and (cadena[i + 1].islower() == True or cadena[i + 1].isupper() == True):
                print("Caracter: %d: no puede llevar un caracter despues de la coma." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(2)

        #   Aqui se manejan las reglas para el guion -********************************************

        if cadena[i] == '-':
            if i < j - 1 and signos1.__contains__(cadena[i + 1]) == True:
                print("Caracter: %d: el guion no puede ir seguido de otro signo." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(3)
            if i > 0 and signos.__contains__(cadena[i - 1]) == True:
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

        if cadena[i] == ':':
            if i < j - 1 and signos.__contains__(cadena[i + 1]) == True:
                print("Caracter: %d: el doble punto no puede ir seguido de otro signo." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(4)
            if i > 0 and (cadena[i - 1].isupper() == False and cadena[i - 1].islower() == False and cadena[i - 1] != '.'):
                print("Caracter: %d: caracter no valido antes del doble punto." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(4)

        #   Aqui se manejan las reglas para el punto y coma ;********************************************

        if cadena[i] == ';':
            if i == 0:
                print("Caracter: %d: el punto y coma no puede ir al inicio de una oración." % i)
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(5)
            if i > 0 and cadena[i - 1].isspace() == True:
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

        if cadena[i] == '"':
            if len(piladc) == 0:
                piladc.append(i)
            elif len(piladc) > 0:
                piladc.pop()

            if len(piladc) == 1 and i > 0 and (signos4.__contains__(cadena[i - 1]) ==  # Antes de abrir "
                                        True or cadena[i - 1].isalpha() == True
                                        or cadena[i - 1].isupper() == True or
                                        cadena[i - 1].islower() == True):
                print("Caracter: %d: la doble comilla no puede ir despues de %s." % (i, cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(6)

            if len(piladc) == 1 and 0 < i < j-1 and signos5.__contains__(cadena[i + 1]) == True:  # Despues de abrir "
                print("Caracter: %d: la doble comilla no puede ir antes de %s." % (i, cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(6)

            if len(piladc) == 0 and i < j - 1 and (signos3.__contains__(cadena[i + 1]) ==  # Despues de cerrar "
                                            True or cadena[i + 1].isalpha() == True
                                            or cadena[i + 1].isupper() == True or
                                            cadena[i + 1].islower() == True):
                print("Caracter: %d: la doble comilla no puede ir antes de %s." % (i, cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(6)

            if len(piladc) == 0 and i < j - 1 and signos5.__contains__(cadena[i - 1]) == True:  # Antes de cerrar "
                print("Caracter: %d: la doble comilla no puede ir despues de %s." % (i, cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(6)

        #if auxcda != 0 and i == j - 1:  # Se muestra la posicion en caso de que las comillas dobles no se hayan cerrado
            #print("Caracter: %d: la doble comilla no se cerró." % auxcda)
            #aerr.append(cadena[auxcda])
            #aerr.append(auxcda)
            #aerr.append(6)

        #   Aqui se manejan las reglas para ( ) ¿ ? y ¡ !********************************************

        if cadena[i] == '(' or cadena[i] == '¿' or cadena[i] == '¡':

            if 0 < i and (signos4.__contains__(cadena[i - 1]) ==  # Antes de abrir (
                        True or cadena[i - 1].isalpha() == True
                        or cadena[i - 1].isupper() == True or
                        cadena[i - 1].islower() == True):
                print("Caracter: %d: el signo %s no puede ir despues de %s." % (i, cadena[i], cadena[i - 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(7)

            if 0 < i and signos6.__contains__(cadena[i + 1]) == True:  # Despues de abrir (
                print("Caracter: %d: el signo %s no puede ir antes de %s." % (i, cadena[i], cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(7)

        if cadena[i] == ')' or cadena[i] == '?' or cadena[i] == '!':

            if i < j - 1 and signos6.__contains__(cadena[i - 1]) == True:  # Antes de cerrar "
                print("Caracter: %d: el signo %s no puede ir despues de %s." % (i, cadena[i], cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(7)

            if i < j - 1 and (signos3.__contains__(cadena[i + 1]) ==  # Despues de cerrar "
                            True or cadena[i + 1].isalpha() == True
                            or cadena[i + 1].isupper() == True or
                            cadena[i + 1].islower() == True):
                print("Caracter: %d: el signo %s no puede ir antes de %s." % (i, cadena[i], cadena[i + 1]))
                aerr.append(cadena[i])
                aerr.append(i)
                aerr.append(7)

        if signos7.__contains__(cadena[i]) == True:  # Para verificar que se abra y cierre correctamente cada signo
            a1 = 0
            c = cadena[i]

            while len(pilac) > 0 and a1 == 0:
                if (c == '?' and pilac.__contains__('¿') == False) or \
                        (c == '!' and pilac.__contains__('¡') == False) or \
                        (c == ')' and pilac.__contains__('(') == False):
                    print("En la posición %d el signo %s se usó sin cerrar" % (i, c))
                    aerr.append(i)
                    aerr.append(8)
                    a1 = 1
                    break

                elif c == '"' and pilac.__contains__('"') == False:
                    pilac.append(c)
                    pilan.append(i)
                    a1 = 1

                elif c == '¿' or c == '¡' or c == '(':
                    pilac.append(c)
                    pilan.append(i)
                    a1 = 1

                elif (c == '?' and pilac[len(pilac) - 1] == '¿') or \
                        (c == '!' and pilac[len(pilac) - 1] == '¡') or \
                        (c == ')' and pilac[len(pilac) - 1] == '(') or \
                        (c == '"' and pilac[len(pilac) - 1] == '"'):
                    pilac.pop()
                    pilan.pop()
                    # a1 = 1
                    a1 = 1

                elif (c == '?' and pilac[len(pilac) - 1] != '¿') or \
                        (c == '!' and pilac[len(pilac) - 1] != '¡') or \
                        (c == ')' and pilac[len(pilac) - 1] != '(') or \
                        (c == '"' and pilac[len(pilac) - 1] != '"'):
                    print("En la posición %d el signo %s está mal implementado" % (
                        pilan[len(pilan) - 1], pilac[len(pilac) - 1]))
                    aerr.append(pilac[len(pilac) - 1])
                    aerr.append(pilan[len(pilan) - 1])
                    aerr.append(8)
                    pilac.pop()
                    pilan.pop()

                if len(pilac) == 0:
                    a1 = 1

            if len(pilac) == 0 and a1 == 0:
                if c == '?' or c == '!' or c == ')':
                    print("En la posición %d el signo %s se usó sin abrir" % (i, c))
                    aerr.append(c)
                    aerr.append(i)
                    aerr.append(8)

                elif c == '¿' or c == '¡' or c == '"' or c == '(':
                    pilac.append(c)
                    pilan.append(i)

    """if cadena[len(cadena) - 1] != '.':  # Si el texto no termina en punto manda error
        print("Al final el texto debe llevar un punto.")
        aerr.append(cadena[i])
        aerr.append(i)
        aerr.append(1)"""

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
# Definir una función denominada retorno_mensaje que retorne siguiente mensaje:
# “Estudiando Fundamentos de Informática en la UNAJ”.

# A. ¿Cómo hago para mostrar ese mensaje en pantalla?
# B. ¿Qué diferencia encuentra con el ejercicio anterior?
# C. Si tuvieras que imprimir mensajes como “Estudiando Matemática I en la UNAJ“ y
# “Estudiando Python en la UNAJ” utilizando la misma función ¿Cómo la modificarías?

opcion = int (input("Ingrese el número 1 para imprimir por pantalla: “Estudiando Matemática I en la UNAJ“ n\ Ingrese el número 2 para imprimir por pantalla “Estudiando Python en la UNAJ”:  "))

def retorno_mensaje():
    if opcion == 1:
        print ("Estudiando Fundamentos de Informática en la UNAJ")
    else:
        if opcion == 2:
            print("Estudiando Python en la UNAJ")
        else:
             print ("Vuelve a intentarlo, la opción ingresada no es válida.")
    return 



retorno_mensaje()

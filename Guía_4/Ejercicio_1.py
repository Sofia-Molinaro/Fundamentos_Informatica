# Escribir un programa que lee un número ingresado por el usuario en pantalla
# y muestre si es positivo, negativo o cero

def positivoNegativoCero(num):
    if num > 0:
        print("Es POSITIVO.")
    elif num == 0:
        print("Es CERO.")
    else:
        print("Es NEGATIVO.")
    return num

numero = int(input("Número: "))
positivoNegativoCero(numero)
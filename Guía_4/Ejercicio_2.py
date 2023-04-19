#​Escribir un programa que me indique si un número es divisible por 6

def divisiblePorSeis(dividendo):
    if dividendo % 6 == 0:
        return True
    else:
        return False

numero = int(input("Número: "))
print(divisiblePorSeis(numero))
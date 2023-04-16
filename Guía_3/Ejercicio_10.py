# Definir una función que calcule el área de un círculo, otra que calcule el área de un rectángulo, otra que calcule el área de un triángulo y otra que calcule el área de un cuadrado. Analice qué parámetros deberían recibir dichas
# funciones.
import math


def calcularAreaDeCirculo(radio):
    areaCirculo = radio * radio * math.pi 
    print(f"El área del círculo es: {areaCirculo} cm²")
    return areaCirculo

def calcularAreaDeRectangulo(baseRectangulo, alturaRectangulo):
   area = base * altura
   print(f"El área del rectángulo es: {areaRectangulo} cm²")
   return area

def calcularAreaDeTriangulo(base, altura):
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area} cm²")

def calcularAreaDeCuadrado(lado):
    area = lado * lado
    print(f"El área del cuadrado es: {area} cm²")
    return area

print("Ingrese una opción para calcular el área de una figura geométrica determinada: \n👉 Opción 1: calcula el área de un círculo \n👉 Opción 2: calcula el área de un rectángulo \n👉 Opción 3: calcula el área de un triángulo \n👉 Opción 4: calcula el área de un cuadrado")

opciones = input("Opción: ")

if opciones == '1':
    radio = float(input("Ingrese el radio del círculo en cm. : "))
    calcularAreaDeCirculo(radio)

elif opciones == '2':
    baseRectangulo = float(input("Ingrese la medida de la base del rectángulo en cm. : "))
    alturaRectangulo = float(input("Ingrese la medida de la altura del rectángulo en cm. : "))
    calcularAreaDeRectangulo(baseRectangulo, alturaRectangulo)
    
elif opciones == '3':
    baseTriangulo = float(input("Ingrese la medida de la base del triángulo en cm. : "))
    alturaTriangulo = float(input("Ingrese la medida de la altura del triángulo en cm. : "))
    calcularAreaDeTriangulo(baseTriangulo, alturaTriangulo)

elif opciones == '4':
    ladoCuadrado = float(input("Ingrese la medida de un lado del cuadrado en cm. : "))
    calcularAreaDeCuadrado(ladoCuadrado)
else:
    print("inténtelo nuevamente. La opción ingresada no es válida. ")
# Definir una función que calcule el área de un círculo, otra que calcule el área de un rectángulo, otra que calcule el área de un triángulo y otra que calcule el área de un cuadrado. Analice qué parámetros deberían recibir dichas
# funciones.
import math


def calcularAreaDeCirculo():
    radio = float(input("Ingrese el radio del círculo en cm. : "))
    areaCirculo = 2 * math.pi * radio
    print(f"El área del círculo es: {areaCirculo} cm²")
    return areaCirculo

def calcularAreaDeRectangulo():
   baseRectangulo = float(input("Ingrese la medida de la base del rectángulo en cm. : "))
   alturaRectangulo = float(input("Ingrese la medida de la altura del rectángulo en cm. : "))
   areaRectangulo = baseRectangulo * alturaRectangulo
   print(f"El área del rectángulo es: {areaRectangulo} cm²")
   return areaRectangulo

def calcularAreaDeTriangulo():
    baseTriangulo = float(input("Ingrese la medida de la base del triángulo en cm. : "))
    alturaTriangulo = float(input("Ingrese la medida de la altura del triángulo en cm. : "))
    areaTriangulo = (baseTriangulo * alturaTriangulo) / 2
    print(f"El área del triángulo es: {areaTriangulo} cm²")

def calcularAreaDeCuadrado():
    ladoCuadrado = float(input("Ingrese la medida de un lado del cuadrado en cm. : "))
    areaCuadrado = ladoCuadrado * ladoCuadrado
    print(f"El área del cuadrado es: {areaCuadrado} cm²")
    return areaCuadrado

print("Ingrese una opción para calcular el área de una figura geométrica determinada: \n👉 Opción 1: calcula el área de un círculo \n👉 Opción 2: calcula el área de un rectángulo \n👉 Opción 3: calcula el área de un triángulo \n👉 Opción 4: calcula el área de un cuadrado")

opciones = input("Opción: ")

if opciones == '1':
    calcularAreaDeCirculo()
elif opciones == '2':
    calcularAreaDeRectangulo()
elif opciones == '3':
    calcularAreaDeTriangulo()
elif opciones == '4':
    calcularAreaDeCuadrado()
else:
    print("inténtelo nuevamente. La opción ingresada no es válida. ")

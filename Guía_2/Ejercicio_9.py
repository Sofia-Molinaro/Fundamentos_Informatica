# Pedir alto, ancho y largo de una pileta. Calcular el volumen y la cantidad de litros
# que tiene. (saber que 1000 cm3=1 litro)
alto = float(input("Ingrese el alto de una pileta: "))
ancho = float((input("Ingrese el ancho de una pileta: ")))
largo = float((input("Ingrese el largo de una pileta: ")))
volumen = ancho * alto * largo
cantidadLitros = volumen / 1000
print(f"El volumen de la pileta es de {volumen} cm3 y la cantidad de litros es {cantidadLitros}.")
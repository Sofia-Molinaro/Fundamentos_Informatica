# Diseña un programa que, a partir del valor del lado de un cuadrado (3 metros),
# muestre el valor de su perímetro (en metros) y el de su área (en metros cuadrados). (El perímetro
# debe darte 12 metros y el área 9 metros cuadrados.)

lado = float(input("Ingrese la medida del lado de un cuadrado: "))
perimetro = lado * 4
area = lado * lado
print(f"El perímetro del cuadrado es de: {perimetro} cm y el área es de: {area} cm2")
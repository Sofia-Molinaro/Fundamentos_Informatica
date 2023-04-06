#Pedir que se ingrese 3 notas e imprimir el promedio. Recordar que el promedio es la suma de los números dividido la cantidad.
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio de las notas {nota1}, {nota2}, {nota3} es de: {promedio}")
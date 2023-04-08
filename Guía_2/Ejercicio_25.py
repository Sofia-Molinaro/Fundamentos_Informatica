# Escriba un programa que reciba un nombre y una edad ingresado por el usuario e
# imprima en la pantalla un texto con la información ingresada por el usuario.
# En pantalla debe aparecer “ Su nombre es xxx y su edad es xx”
# ¿Hizo uso de variables? ¿Cuáles? Sí. utilicé las variables nombre y edad. 
# ¿Hizo uso de valores? ¿Cuáles? Los valores de nombre y edad serán ingresados por el usuario. 
# ¿Hizo uso de operadores? ¿Cuáles?  Utilicé el operador suma (+) para concatenar los strings.
# ¿Qué sentencias utilizó? Utilicé input y print

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
print('Su nombre es' + nombre + 'y su edad es' + edad)
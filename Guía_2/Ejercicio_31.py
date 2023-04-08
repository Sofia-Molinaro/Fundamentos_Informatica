#Pedir el cuit que tiene la siguiente forma xx/dni/x. Extraer y mostrar el dni.
cuit = input("Ingrese su número de cuit: ")
dni = cuit[2:9]
print(f"Su D.N.I. es: {dni}")
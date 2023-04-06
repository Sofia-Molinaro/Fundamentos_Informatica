# Pedir 2 números y mostrar la división entre ellos y el resto.
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número distinto de cero: ")) 
division = numero1 // numero2
resto = numero1 - (division * numero2) 
print(f"El resto de la división entre {numero1} y {numero2} es {resto}")
#Pedir tres palabras y mostrar un texto con las iniciales de las tres.
primeraPalabra = input("Ingrese la primera palabra: ")
segundaPalabra = input("Ingrese la segunda palabra: ")
terceraPalabra = input("Ingrese la tercera palabra: ")

texto = f"""
Iniciales de las palabras ingresadas por teclado:
1er palabra: {primeraPalabra} 👉 Inicial: {primeraPalabra[0]}
2da palabra: {segundaPalabra} 👉 Inicial: {segundaPalabra[0]}
3er palabra: {terceraPalabra} 👉 Inicial: {terceraPalabra[0]}
"""

print(texto)
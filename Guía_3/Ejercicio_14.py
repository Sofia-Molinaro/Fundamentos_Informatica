# Definir una función llamada armo_cartel que reciba una cadena de caracteres (para el
# nombre del producto) y dos números (el precio anterior y el otro para el precio rebajado) e imprima un
# cartel de la siguiente forma:
# *************************************
# 

def armo_cartel(nombreDelProducto, precioAnterior, precioRebajado):
    print(f"*************************************\n Atención!!! Gran rebaja para el producto nombre {nombreDelProducto}, \n Antes: precio anterior ${precioAnterior}, \n Ahora: precio rebajado ${precioRebajado}")
    return nombreDelProducto, precioAnterior, precioRebajado

nombreProducto = input("Ingrese el nombre del producto: ")
precioAnterior = float(input("Ingrese el precio anterior del producto: "))
precioRebajado = float(input("Ingrese el precio rebajado del producto: "))

armo_cartel(nombreProducto, precioAnterior, precioRebajado)
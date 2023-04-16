# Definir una función llamada calculo_nuevo_precio que reciba dos números, uno con el
# precio anterior y otro con el número de porcentaje a aumentar y devuelva el precio aumentado.

def calculo_nuevo_precio(precioAnterior, porcentajeAumentar):
    precioAumentado =  ((porcentajeAumentar * precioAnterior) / 100) + precioAnterior
    print(f"El precio aumentado es: ${precioAumentado}")
    return precioAumentado 

precio_anterior = float(input("Ingrese el precio anterior: $"))
porcentaje_a_aumentar = float(input("Ingrese el porcentaje a aumentar: "))

calculo_nuevo_precio(precio_anterior, porcentaje_a_aumentar)
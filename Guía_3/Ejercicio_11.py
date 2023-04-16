# Definir una función llamada calculo_rebaja que reciba dos números, uno con el precio anterior y otro para el precio rebajado y devuelva un número que represente el porcentaje rebajado.

def calculo_rebaja(precioSinDescuento, precioConDescuento):
    porcentajeRebajado = (precioConDescuento * 100) / precioSinDescuento
    print (f"El porcentaje rebajado es : {porcentajeRebajado}%")
    return porcentajeRebajado

sinDescuento = float(input("Ingrese el precio del producto SIN el descuento: "))
conDescuento = float(input("Ingrese el precio del producto con el descuento: "))

calculo_rebaja(sinDescuento, conDescuento)
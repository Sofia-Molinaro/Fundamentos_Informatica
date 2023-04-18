# Definir una función llamada a_pagar que reciba 4 números: la cantidad de personas, el
# monto gastado en bebida, el monto gastado en comida y el del alquiler del lugar, y retorne cuánto le
# toca pagar a cada uno.

def a_pagar(cantidadPersonas, montoBebidas, montoComida, montoAlquiler):
    montoTotal = (montoBebidas + montoComida + montoAlquiler) / cantidadPersonas
    print(f"El total que debe pagar cada uno es: ${montoTotal}")
    return montoTotal

cant_personas = int(input("Ingrese la cantidad de personas: "))
monto_gastado_bebidas = float(input("Ingrese el monto gastado en bebidas: "))
monto_gastado_comida = float(input("Ingrese el monto gastado en comida: "))
monto_gastado_alquiler = float(input("Ingrese el monto gastado en el alquiler: "))

a_pagar(cant_personas, monto_gastado_bebidas, monto_gastado_comida, monto_gastado_alquiler)
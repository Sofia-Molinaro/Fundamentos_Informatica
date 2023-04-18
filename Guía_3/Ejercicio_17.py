# Definir tres funciones llamadas convertir_a_dolar, convertir_a_euro y
# convertir_a_real. Cada función recibe un parámetro que representa un monto en pesos y devuelve su
# conversión respectiva.

def convertir_a_dolar(montoPesos):
    dolar = montoPesos / 222.5
    print(f"El monto ingresado de ${montoPesos} son USD${dolar}")
    return dolar

def convertir_a_euro(montoPesos):
    euro = montoPesos / 237.54 
    print(f"El monto ingresado de ${montoPesos} son €{euro}")
    return euro

def convertir_a_real(montoPesos):
    real = montoPesos / 43.59
    print(f"El monto ingresado de ${montoPesos} son R${real}")
    return real

monto_pesos = float(input("Ingrese el monto de pesos a convertir a dólares: "))
convertir_a_dolar(monto_pesos)
monto_pesos = float(input("Ingrese el monto de pesos a convertir a euros: "))
convertir_a_euro(monto_pesos)
monto_pesos = float(input("Ingrese el monto de pesos a convertir a reales: "))
convertir_a_real(monto_pesos)
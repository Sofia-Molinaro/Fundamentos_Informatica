# ​Dada la siguiente tabla

# Transporte   #Pasajeros
# Bicicleta     1
# Moto          2
# Auto          4
# Camioneta     12
# Colectivo     40
# Avión         200

# Escribir un programa que dada la cantidad de personas a viajar, determine el
# medio de transporte.

def transporteSegunLaCantidadDePersonas(cantidadDePersonas):
    if cantidadDePersonas == 1:
        respuesta = "Bicicleta"
    elif cantidadDePersonas == 2:
        respuesta = "Moto"
    elif cantidadDePersonas <= 4:
        respuesta = "Auto"
    elif cantidadDePersonas <= 12:
        respuesta = "Camioneta"
    elif cantidadDePersonas <= 40:
        respuesta = "Colectivo"
    elif cantidadDePersonas <= 200:
        respuesta = "Avión"
    else:
        respuesta = "Inténtelo nuevamente."
        return respuesta

personas = int(input ("Ingrese la cantidad de personas que va a viajar: "))
print(transporteSegunLaCantidadDePersonas(personas))
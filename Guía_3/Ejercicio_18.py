# Definir una función llamada calculo_dosis que reciba tres números. Uno para la cantidad
# de días que debe suministrarse el remedio, el segundo dato para la cantidad de veces por día que debe
# tomarlo, y el último dato para la cantidad de comprimidos que trae el envase. La función debe devolver
# verdadero si el envase alcanza para ese tratamiento y falso si no alcanza.

def calculo_dosis(cantidadDias, cantidadVecesPorDia, cantidadComprimidosEnvase):
    respuesta = cantidadDias * cantidadVecesPorDia - cantidadComprimidosEnvase
    
    if respuesta > 0:
        print("FALSO. El envase NO alcanza para ese tratamiento.")
        return False
    elif respuesta == 0:
        print("VERDADERO. Los comprimidos le alcanzan justo para el tratamiento.")
        return True
    else:
        print ("VERDADERO. El envase alcanza para ese tratamiento.")
        return True


cantidadDias = int(input("Ingrese la cantidad de días que dura el tratamiento: "))
cantidadVecesPorDia = int(input("Ingrese la cantidad de veces al día que debe realizar el tratamiento: "))
cantidadComprimidosPorEnvase = int(input("Ingrese la cantidad de comprimidos que trae el envase: "))

calculo_dosis(cantidadDias, cantidadVecesPorDia, cantidadComprimidosPorEnvase)
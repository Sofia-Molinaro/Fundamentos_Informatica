# Definir una función llamada calculo_litros que reciba tres números, el alto, ancho y
# profundidad (en metros) de una pileta y devuelva la cantidad de litros que tiene.

def calculo_litros(alto, ancho, profundidad):
    cantidadLitros = alto * ancho * profundidad
    print(f"La cantidad de litros de la pileta son: {cantidadLitros} metros.")
    return cantidadLitros


altoEnMetros = float(input("Altura de la pileta en metros: "))
anchoEnMetros = float(input("Ancho de la pileta en metros: "))
profundidadEnMetros = float(input("Profundidad de la pileta en metros: "))

calculo_litros(altoEnMetros, anchoEnMetros, profundidadEnMetros)
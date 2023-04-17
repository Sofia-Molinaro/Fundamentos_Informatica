# Definir una función llamada calculo_transporte que reciba cuatro números: la cantidad
# de alumnos de 1era, 2da y 3er. salita de un jardín de infantes y la cantidad de asientos del transporte
# escolar. La función debe retornar cuántos micros necesito contratar para una excursión sabiendo que
# cada salita es acompañada por tres adultos.

def calculo_transporte(cantidadAlumnos):
    cantidadAsientos = 37
    docentes = 3
    cantidadMicros = (cantidadAlumnos + docentes) // cantidadAsientos 
    print(f"La cantidad de micros que se necesitan es: {cantidadMicros} micros.")
    return cantidadMicros


cantidad_Salita_Primera = int(input("Ingrese los alumnos de la primera salita de jardín de infantes: "))
calculo_transporte(cantidad_Salita_Primera)
cantidad_Salita_Segunda = int(input("Ingrese los alumnos de la segunda salita de jardín de infantes: "))
calculo_transporte(cantidad_Salita_Segunda)
cantidad_Salita_Tercera = int(input("Ingrese los alumnos de la tercera salita de jardín de infantes: "))
calculo_transporte(cantidad_Salita_Tercera)
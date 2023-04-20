# Diseñar un programa que dado un número de 1 a 7 determine el día de la
# semana que representa: 1- Domingo a 7 – Sábado. ¿Qué pasa si ingreso un número
# mayor que 7?

def diasDeLaSemana(nro_dia):
    """Determina el día de la semana según el número dado por parámetro.
    1- Domingo
    2 - Lunes
    ...
    """
    dias_semana = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
    return dias_semana[nro_dia-1]

numero = int(input("Número: "))
print(diasDeLaSemana(numero))
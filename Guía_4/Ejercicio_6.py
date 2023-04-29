# Desarrollar un programa en el ingrese un año de nacimiento y me indique si
# la persona es bebé, menor, adolescente, adulto, veterano, abuelo

# Tipo            Edad

# Bebé           < 2 años
# Menor          > 2 y <=12
# Adolescente    >12 y <=18
# Adulto         >18 y <=45
# Veterano       >45 y <=60
# Abuelo         >60

def edadPersona(edad):
    if edad < 2:
        resultado = "Bebé"
    elif edad <= 12:
        resultado = "Menor"
    elif 12 < edad <= 18:
        resultado = "Adolescente"
    elif 18 < edad <= 45:
        resultado = "Adulto"
    elif 45 < edad <= 60:
        resultado = "Veterano"
    elif edad > 60: 
        resultado = "Abuelo"
    return resultado

def aniosPersona(anios):
    anios = 2023 - anios
    return anios

anioDeNacimiento = int(input("Ingrese el año de nacimiento de la persona: "))

anios = aniosPersona(anioDeNacimiento)
print(anios)
print(edadPersona(anios))

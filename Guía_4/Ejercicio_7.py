# ​Dada la siguiente tabla

# Sexo          Altura (cm)
# Femenino      < 145 cm      Petisa
# Femenino      >145 y <170   Normal
# Femenino      >170          Alta

# Masculino     <160 cm       Petisa
# Masculino     >160 y <190   Normal
# Masculino     > 190         Alta

# Escriba un programa que, leyendo del teclado los valores de sexo y altura,
# determine si es una persona petisa, normal o alta.

def datosIngresadosFemenino(altura):
    if altura < 145: 
        resultado = "Petisa"
    elif altura > 145 and altura < 170:
        resultado = "Normal"
    else:
        resultado = "Alta"
    return resultado

def datosIngresadosMasculino(altura):
    if altura < 160: 
        resultado = "Petiso"
    elif altura > 160 and altura < 190:
        resultado = "Normal"
    else:
        resultado = "Alto"
    return resultado

sexoDePersona = input("Ingrese el sexo de la persona('f' para femenino y 'm' para masculino): ")
alturaDePersona = float(input("Altura en cm.: "))

if sexoDePersona == "f":
    print(datosIngresadosFemenino(alturaDePersona))
elif sexoDePersona == "m":
    print(datosIngresadosMasculino(alturaDePersona))
else:
    print("Opción incorrecta. Inténtelo nuevamente.")
# Pedir nombre, apellido de una persona y el día, mes, año en que nació. Armarle una
# clave con esos datos (su clave seria sus iniciales seguido de un guión bajo y de su año de
# nacimiento) y mostrarla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dia =  input("Ingrese su día de nacimiento: ")
mes = input("Ingrese su mes de nacimiento: ")
anio = input("ingrese su año de nacimineto: ")
clave = nombre[0] + apellido[0] + '_' + anio
print(f"Clave: {clave}")
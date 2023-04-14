# Definir una función denominada imprimo_fecha que reciba tres cadenas de caracteres que
# representan un día, un mes y un año e imprima la fecha de la siguiente manera: “ 21 de septiembre de
# 2012”.
d = " " 
m = " " 
a = " " 

def imprimo_fecha(dia, mes, anio):
    dia = int(input("Ingrese un día en números: ")) 
    mes = input("Escriba un mes: ")
    anio = int(input("Ingrese un año: "))
    print(f"{dia} de {mes} de {anio}")
    return

imprimo_fecha(d,m,a)
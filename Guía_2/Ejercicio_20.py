# 20:Ejecutar los siguientes códigos. ¿Cuál es el resultado de las siguientes ejecuciones?.
# Justificar
# a) tupla=(1,True,['a','b','c'], "hola")
# tupla[1]=False
# b) tupla=(1,True,['a','b','c'], "hola")
# tupla[2][0]='b'

# A) No cambia el resultado porque las tuplas son objetos inmutables. 
tupla = (1,True,['a','b','c'], "hola")
#tupla[1] = False
print(tupla)

# B) Cambia el resultado porque las listas son mutables. 
tupla [2][0] = 'b'
print(tupla)
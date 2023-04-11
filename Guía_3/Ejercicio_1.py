#Definición de la función:
#f(x) =  3 * x
def lineal3(x):
    resultado = 3 * x 
    return resultado 

#Uso o invocación de la función
#f(1) = 3 * 1
#f(10) = 3 * 10

print(lineal3(1))
print(lineal3(10))

x=int(input("Ingrese un valor: "))
print(lineal3(x))
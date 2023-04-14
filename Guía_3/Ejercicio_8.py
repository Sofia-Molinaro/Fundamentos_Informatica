# Definir una función denominada cuantos_dias que reciba el número de mes como
# parámetro y retorne la cantidad de días que posee. Ejemplo: cuantos_dias(1), debería retornar 31.
# Ayuda: Pensar en tener una lista de la siguiente manera: [[“enero”,31], [“febrero”, 28], ...]



def cuantos_dias(meses):
   
    meses = [["enero",31], ["febrero", 28], ["marzo", 31], ["abril", 30], ["mayo", 31], ["junio", 30], ["julio", 31], ["agosto", 31], ["septiembre", 30],["octubre", 31], ["noviembre", 30], ["diciembre", 31]]

    for i in range(0, len(meses[0])-1):

        print(meses[i][1])
      
    return meses[i][1]

cantidadDeDiasDelMes = int(input("Ingrese el número del mes (los números enteros que se ingresan van del 1 al 12 inclusive): "))

cuantos_dias(cantidadDeDiasDelMes) 

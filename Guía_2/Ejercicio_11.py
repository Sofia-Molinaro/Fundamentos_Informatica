# Pedir datos de 4 productos comprados, con su cantidad y precio unitario y mostrar
# cuánto se gasta por cada producto y el total

producto1 = input("Ingrese el nombre del primer producto: ")
cantidad1 = int(input("Ingrese la cantidad del primer producto: "))
precio1 = float(input("Ingrese el precio del primer producto: $"))

producto2 = input("Ingrese el nombre del segundo producto: ")
cantidad2 = int(input("Ingrese la cantidad del segundo producto: "))
precio2 = float(input("Ingrese el precio del segundo producto: $"))

producto3 = input("Ingrese el nombre del tercer producto: ")
cantidad3 = int(input("Ingrese la cantidad del tercer producto: "))
precio3 = float(input("Ingrese el precio del tercer producto: $"))

producto4 = input("Ingrese el nombre del cuarto producto: ")
cantidad4 = int(input("Ingrese la cantidad del cuarto producto: "))
precio4 = float(input("Ingrese el precio del cuarto producto: $"))

gastoPrimerProducto = cantidad1 * precio1
gastoSegundoProducto = cantidad2 * precio2
gastoTercerProducto =  cantidad3 * precio3
gastoCuartoProducto = cantidad4 * precio4
total = gastoPrimerProducto + gastoSegundoProducto + gastoTercerProducto + gastoCuartoProducto

print(f"Se gasta ${gastoPrimerProducto} para el primer producto, ${gastoSegundoProducto} para el segundo producto, ${gastoTercerProducto} para el tercer producto y ${gastoCuartoProducto} para el cuarto producto.")

print(f"El gasto total es de ${total}")
# Definir una función que reciba un número como parámetro y mostrar la tabla de
# multiplicar de dicho número.
def numero_a_multiplicar(num):
    print(f"La tabla de multiplicar del {num} es: ")
    for i in range(1, 11):
        tabla = num * i
        i += 1
        print(f"{num} x {i} es = {tabla}")
    return (tabla)

numeroQueSeMultiplica = int(input("Número: "))
numero_a_multiplicar(numeroQueSeMultiplica)
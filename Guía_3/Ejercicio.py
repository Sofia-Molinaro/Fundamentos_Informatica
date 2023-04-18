#Dada una cadena de texto, comprobar si es un palíndromo o no.

def es_palindromo(palabra):
    if palabra == "":    #caso borde
        return False
    for i in range(0, len(palabra)):
        if palabra[i] != palabra[len(palabra)-i-1]:
            return False 
    return True

palabra = input("Palabra: ")

es_palindromo(palabra)
if es_palindromo(palabra) == True:
    print("La palabra es un palíndromo")
else: 
    print("La palabra NO es un palíndromo")

# print(es_palindromo("ana"))
# print(es_palindromo("anitalavalatina"))
# print(es_palindromo("pablo"))
# print(es_palindromo(""))

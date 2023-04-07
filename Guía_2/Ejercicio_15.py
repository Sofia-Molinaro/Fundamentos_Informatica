#Pedir un verbo en infinitivo y mostrar su terminación (ar, er o ir)
palabra = input("Ingrese un verbo en infinitivo: ")
print(f"La terminación de {palabra} es: {palabra[-2] + palabra[-1]}")
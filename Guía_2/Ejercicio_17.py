# Pedir cuatro datos, quién, qué hizo, cuándo y cómo. Mostrar la siguiente noticia:
# “Última noticia!, la persona xx, en el dia xx, hizo xx, de la siguiente manera xx”

quien = input("Ingrese quién es el protagonista de la noticia: ")
queHizo = input("Indique qué hizo: ")
cuando = input("Ingrese cuándo lo hizo: ")
como = input("Indique cómo lo hizo: ")

print(f"¡Última noticia!, {quien}, en el dia {cuando}, hizo {queHizo}, de la siguiente manera: {como}")
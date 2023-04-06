# Pedir ancho y largo de un terreno y mostrar cuántos paneles de pasto hay que
# comprar (son de 60x60 cm)

ancho = float(input("Ingrese el ancho del terreno: "))
largo = float(input("Ingrese el largo del terreno: "))
paneles = (ancho * largo) // 3600
print(f"Los paneles de pasto que hay que comprar son: {paneles}")
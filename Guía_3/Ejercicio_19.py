# Definir una función llamada precio_con_iva que agrega el IVA (21%) de un producto
# dado su precio de venta sin IVA.

def precio_con_ivaI(precio):
    precioConIVA = (precio * 0.21) + precio
    return precioConIVA

def precio_con_ivaII(precio: float):
    return precio*1.21

precio = float(input("Ingrese el precio de un producto sin IVA: "))
print(f"Precio con IVA: ${precio_con_ivaII(precio)}")
# Pedir el diámetro de un círculo y calcular su área y perímetro. Recordar que
# Perímetro = π * Diámetro , Área = π * radio2. Por último, el diámetro = 2 * radio

import math
diametro = float(input("Ingrese el diámetro de un círculo en cm: "))
radio = diametro / 2
area = math.pi * radio * radio
perimetro = math.pi * diametro
print(f"El área de la circunferencias es {area} cm2 y el perímetro es {perimetro} cm.")
# Escribir un programa que lea dos números “n” y “m” y determine si m es
# divisible por n.

def m_esDivisiblePor_n(m, n):
    if m % n == 0:
        return True
    else:
        return False
    
dividendoM = int(input("Ingrese un número: "))
divisorN = int(input("Ingrese otro número: "))

print(m_esDivisiblePor_n(dividendoM, divisorN))
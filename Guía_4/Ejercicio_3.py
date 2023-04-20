# Escribir un programa que lea dos números “n” y “m” y determine si m es
# divisible por n.

def m_es_divisible_por_n(m, n):
    if m % n == 0:
        return True
    return False
    
def m_es_divisible_por_n_V2(m: int,n: int):
    return m % n == 0
    
dividendoM = int(input("Ingrese un número: "))
divisorN = int(input("Ingrese otro número: "))

print(m_es_divisible_por_n(dividendoM, divisorN))
print(m_es_divisible_por_n_V2(dividendoM, divisorN))
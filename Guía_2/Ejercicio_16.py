# Pedir nombre, apellido, nro. de alumno y comisión que desea suscribirse. Mostrar
# el siguiente mensaje “La solicitud de inscripción a la comisión <comision> solicitada por el
# alumno <apellido>, <nombre> está siendo procesada”

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
comision = int(input("Ingrese su comision: "))

print(f"La solicitud de inscripción a la comisión {comision} solicitada por el alumno {apellido}, {nombre} está siendo procesada.")
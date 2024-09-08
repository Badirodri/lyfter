# 2. Cree un pseudocódigo que le pida un `tiempo en segundos` al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “*Mayor*”.
#     1. *Ejemplos*:
#         1. 1040 → Mayor
#         2. 140 → 460
#         3. 599 → 1

tiempo_segundos = int(input("Digite el tiempo en segundos producto: "))
tiempo_restante = 0

if (tiempo_segundos > 600):
    print("Mayor")
else:
    tiempo_restante= 600 - tiempo_segundos
    print(f"Faltan {tiempo_restante}")
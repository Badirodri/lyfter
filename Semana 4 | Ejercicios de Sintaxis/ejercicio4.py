# Cree un programa que le pida tres números al usuario y muestre el mayor.

mayor = 0
primero = int(input("Digite el primero numero: "))
segundo = int(input("Digite el segundo numero: "))
tercero = int(input("Digite el tercer numero: "))

if (primero > segundo):
    mayor = primero
elif (segundo > tercero):
    mayor = segundo
else:
    mayor = tercero

print (f"El mayor es el {mayor}")
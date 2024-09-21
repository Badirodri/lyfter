# 5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
#     1. Ejemplos:
#     2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

my_list = []
contador = 0
mayor = 0

while (contador < 10):
    my_list.append(int(input("Digite un numero: ")))
    if (my_list[contador]> mayor):
        mayor = my_list[contador]
    contador += 1

print (f"{my_list} y el mayor es {mayor}")

#mayor_solucion2 = my_list.copy()
#mayor_solucion2.sort()
#print (f"{my_list} y el mayor es {mayor_solucion2[-1]}")
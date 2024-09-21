# 3. Cree un algoritmo que le pida un numero al usuario y muestre la suma de todos los números desde 1 hasta ese número.
#     1. 3 → 6 (1 + 2 + 3)
#     2. 5 → 15 (1 + 2 + 3 + 4 + 5)
#     3. 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

numero = int(input("Digite el numero: "))
suma = 0
contador = 1

while (contador <= numero):
    suma= suma + contador
    contador = contador + 1

print(suma)
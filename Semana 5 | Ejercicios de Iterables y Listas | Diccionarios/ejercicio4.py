# 4. Cree un programa que elimine todos los números impares de una lista.
#     1. Ejemplos:
#     2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# No estoy entendiendo porque me retorna error
# si lo recorro de esta forma

#length = len(my_list)
#for index in range(0, length):
#    if ((my_list[index] % 2)!= 0):
#        my_list.pop(index)


for index in range(len(my_list) - 1, -1, -1):
    if (my_list[index] % 2) != 0:
        my_list.pop(index)

print(my_list)
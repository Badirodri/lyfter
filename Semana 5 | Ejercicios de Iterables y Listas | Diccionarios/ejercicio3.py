# 3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
#     1. Ejemplos:
#     2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`

my_list = [4, 3, 6, 1, 7]

first_element = my_list.pop(0)
last_element = my_list.pop(-1)

my_list.append(first_element)
my_list.insert(0, last_element)

print(my_list)
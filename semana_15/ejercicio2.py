# 2. Modifica el `bubble_sort` para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).
#    Este hace lo mismo que el resto, solo que recorre la lista de derecha a izquierda, y las “burbujas” son los elementos menores, no los mayores.

def bubble_sort_reversed(list_to_sort):
  for outer_index in range(len(list_to_sort)):
    for index in range(len(list_to_sort) - 1, outer_index, -1):
      current_element = list_to_sort[index]
      next_element = list_to_sort[index -1]

      if current_element > next_element:
        list_to_sort[index]= next_element
        list_to_sort[index - 1] = current_element


      print(f'Elemento actual: {current_element}, Siguiente elemento: {next_element}')


my_test_list = [18, -11, 68, 6, 32, 53, -2]
bubble_sort_reversed(my_test_list)

print(my_test_list)
# 1. Crea un `bubble_sort` por tu cuenta sin revisar el código de la lección.
def bubble_sort(list_to_sort):
  for outer_index in range(0, len(list_to_sort)-1):
    for index in range(0, len(list_to_sort)-1 - outer_index):
      current_element = list_to_sort[index]
      next_element = list_to_sort[index + 1]

      if current_element > next_element:
        list_to_sort[index]= next_element
        list_to_sort[index+ 1] = current_element

      print(f'-- Iteracion {outer_index} {index}. Elemento actual: {current_element}, Siguiente elemento: {next_element}')



my_test_list = [18, -11, 68, 6, 32, 53, -2]
bubble_sort(my_test_list)

print(my_test_list)
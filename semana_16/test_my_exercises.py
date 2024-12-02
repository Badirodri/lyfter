from my_exercises import suma_de_la_lista, vuelve_un_string, words_sort

def test_suma_de_la_lista_sums_all_items():
  # Arrange
  input_list = [2, 1, 3]
  # Act
  result = suma_de_la_lista(input_list)
  # Assert
  assert result == 6

def test_vuelve_un_string_reverts_string_order():
  # Arrange
  my_string = 'Hola'
  # Act
  result = vuelve_un_string(my_string)
  # Assert
  assert result == 'aloH'

def test_words_sort_sort_text_properly_sorting_them_in_a_new_list():
  # Arrange
  my_string = 'python-variable-funcion-computadora-monitor'
  # Act
  result = words_sort(my_string)
  # Assert
  assert result == ['computadora', 'funcion', 'monitor', 'python', 'variable']
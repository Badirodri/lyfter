# 1. Cree los siguientes unit tests para el algoritmo `bubble_sort`:
#     1. Funciona con una lista pequeña.
#     2. Funciona con una lista grande (de más de 100 elementos.
#     3. Funciona con una lista vacía.
#     4. No funciona con parámetros que no sean una lista.

import pytest
from my_exercises import bubble_sort

def test_bubble_sort_sorting_properly_small_list_():
  # Arrange
  input_list = [4, 2, 1, 8, 2, 3]
  input_list_sorted = sorted(input_list)
  # Act
  result = bubble_sort(input_list)
  # Assert
  assert result == input_list_sorted


def test_bubble_sort_sorting_properly_big_list_():
  # Arrange
  input_list = [506, 398, 839, 942, 277, 417, 800, 472, 762, 32, 458, 455, 72, 954, 667, 987, 716, 214, 718, 53, 575, 235, 588, 724, 635, 791, 83, 577, 983, 981, 30, 913, 112, 168, 689, 774, 43, 467, 199, 233, 809, 460, 656, 221, 47, 698, 953, 397, 26, 730, 352, 324, 278, 779, 75, 156, 368, 473, 727, 121, 91, 486, 530, 329, 215, 409, 117, 794, 134, 83, 915, 36, 426, 576, 395, 712, 343, 271, 818, 598, 586, 824, 547, 272, 607, 228, 954, 761, 506, 656, 508, 768, 134, 50, 34, 957, 436, 150, 209, 126, 475, 441, 773, 217, 450, 784, 93, 168]

  input_list_sorted = sorted(input_list)
  # Act
  result = bubble_sort(input_list)
  # Assert
  assert result == input_list_sorted

def test_bubble_sort_sorting_properly_empty_list_():
  # Arrange
  input_list = []

  # Act
  result = bubble_sort(input_list)
  # Assert
  assert result == input_list

def test_bubble_sort_raise_value_error():
  # Arrange
  input_list = {}

  # Act and Assert
  with pytest.raises(ValueError):
    bubble_sort(input_list)

# 1. Analice el algoritmo de `bubble_sort` usando la Big O Notation.
# 2. Analice los siguientes algoritmos usando la Big O Notation:


    #  - **bubble_sort** --> # O(n^2)
    def bubble_sort(list_to_sort):
      for outer_index in range(0, len(list_to_sort)-1): # O(n)
        for index in range(0, len(list_to_sort)-1 - outer_index): # O(n^2)
          current_element = list_to_sort[index]
          next_element = list_to_sort[index + 1]

          if current_element > next_element:
            list_to_sort[index]= next_element
            list_to_sort[index+ 1] = current_element



    #  - **print_numbers_times_2** --> # O(n)
    def print_numbers_times_2(numbers_list):
    	for number in numbers_list:
    		print(number * 2)


    # - **check_if_lists_have_an_equal** -->  O(n^2)


    def check_if_lists_have_an_equal(list_a, list_b):
    	for element_a in list_a: # O(n)
    		for element_b in list_b:#  O(n^2)
    			if element_a == element_b:
    				return True

    	return False


    # - **print_10_or_less_elements** --> # O(log n)


    def print_10_or_less_elements(list_to_print):
    	list_len = len(list_to_print)
    	for index in range(min(list_len, 10):
    		print(list_to_print[index]


    # - **generate_list_trios** --> # O(n^3)


    def generate_list_trios(list_a, list_b, list_c):
    	result_list = []
    	for element_a in list_a: # O(n)
    		for element_b in list_b: # O(n^2)
    			for element_c in list_c: # O(n^3)
    				result_list.append(f'{element_a} {element_b} {element_c}')

    	return result_list

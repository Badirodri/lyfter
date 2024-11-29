def bubble_sort(list_to_sort):
    if not isinstance(list_to_sort, list):
        raise ValueError("Input must be a list")
    else:
        # Repetimos la iteración de la lista por todos los elementos para moverlos al final
        for outer_index in range(0, len(list_to_sort) - 1):
            # Usamos esta variable para revisar si hemos movido elementos
            has_made_changes = False
            # Le restamos uno al length para parar en el penultimo elemento
            # Usamos el indice exterior para restar las ejecuciones de
            # los elementos que ya estan ordenados al final
            for index in range(0, len(list_to_sort) - 1 - outer_index):
                # Guardamos los valores del elemento actual y el siguiente
                current_element = list_to_sort[index]
                next_element = list_to_sort[index + 1]

                # Si el actual es mayor al siguiente, intercambiamos sus posiciones
                if current_element > next_element:
                    list_to_sort[index] = next_element
                    list_to_sort[index + 1] = current_element
                    has_made_changes = True

            # Si no hemos movido elementos, la lista ya esta ordenada
            if not has_made_changes:
                break

    # Return the sorted list
    return list_to_sort



def suma_de_la_lista(la_lista):
    suma = 0
    for numero in la_lista:
        suma += numero
    return(suma)


def vuelve_un_string(texto):
    new_text=""
    for letter in range (len(texto) -1, -1, -1):
      new_text += texto[letter]
    return(new_text)

def words_sort(words):
    list_of_words=[]
    word=""
    for letter in words:
        if letter == "-":
            list_of_words.append(word)
            word=""
        else:
            word +=letter
    list_of_words.append(word)

    list_of_words.sort()
    return list_of_words

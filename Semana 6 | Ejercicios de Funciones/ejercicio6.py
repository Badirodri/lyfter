# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

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

def concatenar(words_list):
    new_string=""
    for index in range(0,len(words_list)):
        if index +1 < len(words_list):
            new_string+= words_list[index] + "-"
        else:
            new_string+= words_list[index]
    return(new_string)


print(concatenar(words_sort("python-variable-funcion-computadora-monitor")))
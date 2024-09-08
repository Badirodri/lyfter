# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41

lista= [4,6,2,29]

def suma_de_la_lista(la_lista):
    suma = 0
    for numero in la_lista:
        suma += numero
    return(suma)


print(suma_de_la_lista(lista))
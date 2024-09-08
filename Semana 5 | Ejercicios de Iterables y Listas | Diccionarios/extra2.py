# 2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#     1. Ejemplos:
#     2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
#     `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
#     → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`

numero= [1,2,3,4]
palabra=["uno", "dos", "tres", "cuatro"]
diccionario = {}
contador = 0

while (contador < (len(numero))):
    diccionario[numero[contador]] = palabra[contador]
    contador = contador + 1

print (diccionario)
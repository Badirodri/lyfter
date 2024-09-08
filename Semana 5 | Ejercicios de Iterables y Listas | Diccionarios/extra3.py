# 3. Cree un programa que use una lista para eliminar keys de un diccionario.
#     1. Ejemplos:
#     2. `list_of_keys = [’access_level’, ‘age’]`
#     `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
#     → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`

to_remove= ["borrar", "borrar_2"]
original_dic={
			"borrar": "Chao",
			"dos": 2,
			"borrar_2": "Chao chao"
			}


for key in to_remove:
    original_dic.pop(key)

print(original_dic)
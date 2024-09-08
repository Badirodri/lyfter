# 1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
#     1. Debe incluir:
#         1. Nombre
#         2. Género
#         3. Desarrollador
#         4. Clasificación ESRB
#     2. Ejemplo de archivo final:
#         nombre,genero,desarrollador,clasificacion
#         Grand Theft Auto IV,Accion,Rockstar Games,M
#         The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
#         Tony Hawk's Pro Skater 2,Deportes,Activision,T


import csv

headers = (
	'nombre',
	'genero',
	'desarrollador',
	'ESRB',
)

def csv_builder():
    juegos = []

    try:
        cantidad = int(input("Digite la cantidad de juegos a agregar: "))
        for game in range(cantidad):
            nombre = input("Digite el nombre: ")
            genero = input("Digite el género: ")
            desarrollador = input("Digite el desarrollador: ")
            clasificacion = input("Digite la clasificación ESRB: ")

            diccionario_juego = {
                'nombre': nombre,
                'genero': genero,
                'desarrollador': desarrollador,
                'ESRB': clasificacion
            }

            juegos.append(diccionario_juego)

        return juegos

    except ValueError as error:
        print(f'El elemento debe ser un número')
        raise error

def write_csv_file(file_path,headers):
  try:
    data=csv_builder()
    with open(file_path, 'w', encoding='utf-8') as file:
      writer = csv.DictWriter(file, headers)
      writer.writeheader()
      writer.writerows(data)
  except Exception as ex:
    print(f'Ha ocurrido un error: {ex}')


write_csv_file('games.csv', headers)
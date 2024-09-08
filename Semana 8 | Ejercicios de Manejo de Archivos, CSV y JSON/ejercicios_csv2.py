# # 2. Lea sobre el resto de métodos del módulo `csv` [aqui](https://docs.python.org/es/3/library/csv.html) y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por *tabulaciones* en vez de por *comas*.
# #     1. Ejemplo de archivo final:
# nombre	genero	desarrollador	clasificacion
# Grand Theft Auto IV	Accion	Rockstar Games	M
# The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
# Tony Hawk's Pro Skater 2	Deportes	Activision	T


# ... (Siguiendo el ejercicio anterior)

def write_csv_file(file_path,headers):
  try:
    data=csv_builder()
    with open(file_path, 'w', encoding='utf-8') as file:
      writer = csv.DictWriter(file, headers, delimiter=' ')
      writer.writeheader()
      writer.writerows(data)
  except Exception as ex:
    print(f'Ha ocurrido un error: {ex}')
# <aside>
#  **Ejercicios JSON**

# 1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).
# 2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.
# </aside>

import json

pokemones= """[
  {
    "name": {
      "english": "Pikachu"
    },
    "type": [
      "Electric"
    ],
    "base": {
      "HP": 35,
      "Attack": 55,
      "Defense": 40,
      "Sp. Attack": 50,
      "Sp. Defense": 50,
      "Speed": 90
    }
  },
  {
    "name": {
      "english": "Charmander"
    },
    "type": [
      "Fire"
    ],
    "base": {
      "HP": 39,
      "Attack": 52,
      "Defense": 43,
      "Sp. Attack": 60,
      "Sp. Defense": 50,
      "Speed": 65
    }
  },
  {
    "name": {
      "english": "Squirtle"
    },
    "type": [
      "Water"
    ],
    "base": {
      "HP": 44,
      "Attack": 48,
      "Defense": 65,
      "Sp. Attack": 50,
      "Sp. Defense": 64,
      "Speed": 43
    }
  }
]"""

pokemones_python = json.loads(pokemones)

def existentes():
  pokemones_existentes =[]

  for pokemon in range(0, len(pokemones_python)):
    pokemones_existentes.append(pokemones_python[pokemon]['name']['english'])

  return pokemones_existentes

def agregar_nuevo():
  nuevo_pokemon=[
    {
    "name": {
      "english": ""
    },
    "type": [
      ""
    ],
    "base": {
      "HP": 0,
      "Attack": 0,
      "Defense": 0,
      "Sp. Attack": 0,
      "Sp. Defense": 0,
      "Speed": 0
    }
  }
  ]
  nombre= input('Digite el nombre del pokemon en ingles: ')
  tipo= input('Digite el tipo del pokemon: ')
  hp= int(input('Digite el valor de HP del pokemon: '))
  attack= int(input('Digite el valor de Ataque del pokemon: '))
  defense= int(input('Digite el valor de Defensa del pokemon: '))
  sp_attack= int(input('Digite el valor de Sp. de Ataque del pokemon: '))
  sp_defense= int(input('Digite el valor de Sp. de Defensa del pokemon: '))
  speed= int(input('Digite el valor de Velocidad del pokemon: '))


  if nombre in existentes():
    print('El pokemon ya existe, intente nuevamente')
    agregar_nuevo()
  else:
    nuevo_pokemon[0]['name']['english'] = nombre
    nuevo_pokemon[0]['type'][0] = tipo
    nuevo_pokemon[0]['base']['HP'] = hp
    nuevo_pokemon[0]['base']['Attack'] = attack
    nuevo_pokemon[0]['base']['Defense'] = defense
    nuevo_pokemon[0]['base']['Sp. Attack'] = sp_attack
    nuevo_pokemon[0]['base']['Sp. Defense'] = sp_defense
    nuevo_pokemon[0]['base']['Speed'] = speed
  pokemones_python.extend(nuevo_pokemon)

  return pokemones_python

def convertir_json():
  data = agregar_nuevo()
  data_json = json.dumps(data)
  print(data_json)

convertir_json()

# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”

def vuelve_un_string(texto):
    new_text=""
    for letter in range (len(texto) -1, -1, -1):
      new_text += texto[letter]
    return(new_text)

print(vuelve_un_string("Hola mundo"))
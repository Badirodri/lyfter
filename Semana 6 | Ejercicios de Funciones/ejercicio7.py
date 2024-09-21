# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#     1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#     2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#     3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*

def primos(list):
    lista_de_primos=[]
    for item in list:
        if item > 1:
          #sacando el 1 para no considerarlo
          es_primo= True
          for number in range (2,item):
              if item % number == 0:
                es_primo=False
          if es_primo:
             lista_de_primos.append(item)

    return(lista_de_primos)

print(primos([1,2,5, 4, 6, 7, 13, 9, 67]))

# Pase buen rato jugando con este maecillo, al final ya estaba
# muy cansado para crear la funcion si eran primos entonces
# lo deje en una misma
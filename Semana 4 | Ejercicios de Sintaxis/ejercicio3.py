# Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

numero_secreto = "6"
numero_usuario = ""

while (numero_usuario != numero_secreto):
   numero_usuario = input("Digite un numero entre 1 y 10: ")
print (f"El numero secreto era el {numero_secreto}")

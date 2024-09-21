# Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = int(input("Ingrese su edad "))

if (edad <= 3):
    print ("Bebé")
elif (edad <=10):
    print ("Niño")
elif (edad <= 12):
    print ("Pre-Adolescente")
elif (edad <= 18):
    print ("Adolescente")
elif (edad <= 26 ):
    print ("Adulto joven")
elif (edad <= 59):
    print ("Adulto")
else:
    print ("Adulto mayor")
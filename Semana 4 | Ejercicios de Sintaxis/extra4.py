# Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.

primero = int(input("Digite el primero: "))
segundo = int(input("Digite el segundo: "))
tercero = int(input("Digite el tercero: "))

if (primero == 30):
    print("Correcto")
elif (segundo == 30):
    print("Correcto")
elif (tercero == 30):
    print("Correcto")
elif ((primero+segundo+tercero) == 30):
     print("Correcto")
else:
    print("Incorrecto")
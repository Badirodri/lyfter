# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def instrucciones():
    print('''
                -----------
                Suma: Escriba "mas"
                Resta: Escriba "menos"
                Multiplicar: Escriba "por"
                Division: Escriba "entre"
                Borrar resultado: Escriba "iniciar"
                Salir: Escriba "salir"
                -----------
                ''')

def calculadora():
  numero_actual=0
  salir=False
  try:
    while (salir!= True):
      print(f"El numero actual es: {numero_actual}")
      if numero_actual==0:
        numero_actual=int(input("Digite el numero a calcular: "))
        continue
      else:
        numero_solicitado= int(input("Digite el numero a calcular: "))
        instrucciones()
        operacion= input("Con base en las instrucciones mencionadas, favor ingrese la operación deseada: ").lower()

        if operacion=="mas":
          numero_actual+= numero_solicitado
        elif operacion=="menos":
          numero_actual-= numero_solicitado
        elif operacion=="por":
          numero_actual= numero_actual * numero_solicitado
        elif operacion=="entre":
          if numero_solicitado==0:
            raise ZeroDivisionError()
          else:
            numero_actual= numero_actual / numero_solicitado
        elif operacion=="iniciar":
          numero_actual= 0
        elif operacion=="salir":
          break
        else:
          raise ValueError()

  except ValueError as ex:
    print("Error: La opcion no es valida")
    calculadora()
  except ZeroDivisionError as ex:
    print("Error: Division entre cero no es soportada")
    calculadora()

def main():
  try:
    calculadora()
  except Exception as ex:
    print(f'Ha ocurrido un error: {ex}')

main()
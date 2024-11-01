# 2. Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def check_numeric_params(func):
    def wrapper(*args):
        # Verificar argumentos posicionales
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"El argumento {arg} no es un número.")
        return func(*args)

    return wrapper

@check_numeric_params
def sum_numbers(a,b):
  result = a + b
  print (result)

sum_numbers(1,2)
sum_numbers(1,'2')

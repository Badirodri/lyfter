# 1. Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def printer_decorator(func):
    def wrapper(*args):
        print(f"Function args: {args}")
        result = func(*args)
        print(f"Result: {result}")

    return wrapper


@printer_decorator
def sum_numbers(a,b):
  result = a + b
  return result

sum_numbers(1,2)
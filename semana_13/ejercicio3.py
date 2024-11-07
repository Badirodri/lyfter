# 3. Cree una clase de `User` que:
#     - Tenga un atributo de `date_of_birth`.
#     - Tenga un property de `age`.
#     Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date

class User:
  def __init__(self, date_of_birth):
    self.date_of_birth=date_of_birth

  @property
  def age(self):
          #Calculates age from current date
          today = date.today()
          return (
              today.year
              - self.date_of_birth.year
              - (
                  (today.month, today.day)
                  < (self.date_of_birth.month, self.date_of_birth.day)
              )
          )

def validate_user_age(func):
    def wrapper(user,*args):
        if user.age< 18:
            raise ValueError ("Not valid user")
        return func(user, *args)

    return wrapper

@validate_user_age
def access(user):
  print('Valid user')

Juanito = User(date(2020,1,1))
Juan= User(date(1999,1,1))

access(Juanito)
access(Juan)
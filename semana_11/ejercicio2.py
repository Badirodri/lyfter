# 2. Cree una clase de `Bus` con:
#     1. Un atributo de `max_passengers`.
#     2. Un método para agregar pasajeros uno por uno (que acepte una instancia de `Person` como parámetro). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
#     3. Un método para bajar pasajeros uno por uno (en cualquier orden).

class Bus:
  passengers = []

  def __init__(self, max_passengers):
    self.max_passengers = max_passengers

  def add_passenger(self,person):
    if len(self.passengers) >= self.max_passengers:
      print('There is not space in the bus')
    else:
      self.passengers.append(person)

  def remove_passenger(self,person):
    if len(self.passengers) == 0:
      print('There is not any passenger to remove')
    else:
      self.passengers.remove(person)

bus1= Bus(1)
bus1.add_passenger('John')
bus1.add_passenger('Jaime')
print (bus1.passengers)

bus1.remove_passenger('John')

print (bus1.passengers)
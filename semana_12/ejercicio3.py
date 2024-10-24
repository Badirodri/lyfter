# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

class CanFly():
  def fly(self):
    print('You can fly')

class Animals():
  def animal(self):
    print('You are also an animal')

class Birds(CanFly, Animals):
  pass

eagle= Birds()
eagle.fly()
eagle.animal()

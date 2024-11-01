# 2. Cree una clase abstracta de `Shape` que:
#     1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#     2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#     3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod

class Shape(ABC):

  @abstractmethod
  def calculate_perimeter(self):
    pass

  @abstractmethod
  def calculate_area(self):
    pass

class Circle(Shape):
  pi=3.14

  def __init__(self,radius):
    self.radius=radius

  def calculate_perimeter(self):
    perimeter= 2*self.pi* self.radius
    print(f"Perimeter: {perimeter}")

  def calculate_area(self):
    area= self.pi* self.radius* self.radius
    print(f"Area: {area}")

class Square(Shape):

  def __init__(self,side):
    self.side=side

  def calculate_perimeter(self):
    perimeter= 4*self.side
    print(f"Perimeter: {perimeter}")

  def calculate_area(self):
    area= self.side * self.side
    print(f"Area: {area}")

class Rectangle(Shape):

  def __init__(self,side_a, side_b):
    self.side_a=side_a
    self.side_b=side_b

  def calculate_perimeter(self):
    perimeter= (2*self.side_b) + (2*self.side_a)
    print(f"Perimeter: {perimeter}")

  def calculate_area(self):
    area= self.side_a * self.side_b
    print(f"Area: {area}")

circle = Circle(3)
circle.calculate_area()
circle.calculate_perimeter()

square = Square(3)
square.calculate_area()
square.calculate_perimeter()

square = Rectangle(5,2)
square.calculate_area()
square.calculate_perimeter()
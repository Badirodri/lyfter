
# 1. Cree una estructura de objetos que asemeje un Stack.
#     1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
  data: str

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  head: Node

  def __init__(self, head):
    self.head = head

  def print_structure(self):
    current_node = self.head

    while (current_node is not None):
      print(current_node.data)
      current_node = current_node.next

class Stack(LinkedList):

  def pop(self):
    if self.head:
      self.head=self.head.next

  def push(self,new_node):
    new_node.next = self.head
    self.head = new_node



stack = Stack(Node('primer_nodo'))

print("Agregando un elemento")

stack.push(Node("Soy el nuevo nodo!"))
stack.print_structure()

print("Quitando un elemento")

stack.pop()
stack.print_structure()
# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#     1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node:
  data: str

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class DoubleEndedQueue:
  def __init__(self,head):
    self.head = head

  def print_structure(self):
    current_node = self.head

    while (current_node is not None):
      print(current_node.data)
      current_node = current_node.next

  def pop_left(self):
    if self.head:
      self.head=self.head.next

  def pop_right(self):
    current_node = self.head
    while current_node.next and current_node.next.next:
        current_node = current_node.next

    current_node.next = None

  def push_left(self,new_node):
    new_node.next = self.head
    self.head = new_node

  def push_right(self, new_node):
    current_node = self.head

    while current_node.next is not None:
        current_node = current_node.next
    current_node.next = new_node


node_1 = Node('PRIMERO')

double_queue = DoubleEndedQueue(node_1)


print("Agregando un elemento")

double_queue.push_left(Node("Soy el nuevo nodo!"))
double_queue.push_right(Node("Soy el segundo nuevo nodo!"))
double_queue.print_structure()

print("Quitando un elemento")

double_queue.pop_left()
double_queue.pop_right()
double_queue.print_structure()
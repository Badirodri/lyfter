# 3. Cree una estructura de objetos que asemeje un Binary Tree.
#     1. Debe incluir un método para hacer `print` de toda la estructura.
#     2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
  data: str

  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

class BinaryTree:
  def __init__(self,head):
    self.head = head

  def print_structure(self):
    current_node = self.head

    while (current_node is not None):
      print(current_node.data)
      current_node = current_node.left

  def pop_left(self):
    if self.head:
      self.head=self.head.left

  def pop_right(self):
    current_node = self.head
    while current_node.left and current_node.left.left:
        current_node = current_node.left

    current_node.left = None

  def push_left(self,new_node):
    new_node.left = self.head
    self.head = new_node

  def push_right(self, new_node):
    current_node = self.head

    while current_node.left is not None:
        current_node = current_node.left
    current_node.left = new_node


node_1 = Node('PRIMERO')

double_queue = BinaryTree(node_1)


print("Agregando un elemento")

double_queue.push_left(Node("Soy el nuevo nodo!"))
double_queue.push_right(Node("Soy el segundo nuevo nodo!"))
double_queue.print_structure()

print("Quitando un elemento")

double_queue.pop_left()
double_queue.pop_right()
double_queue.print_structure()
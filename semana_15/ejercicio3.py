# Implemente un `bubble_sort` que funcione para Linked Lists
# La lógica es la misma. Solo que intercambiar los elementos lleva su propio proceso.

class Node:
  data: str
  next: "Node"

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  head: Node

  def __init__(self, head):
    self.head = head


  def print_structure(self):
    current_node = self.head
    while current_node is not None:
        # Imprimir el nodo y la flecha, si no es el último nodo
        if current_node.next:
            print(f"{current_node.data} -> ", end="")
        else:
            print(current_node.data)  # Último nodo sin flecha
        current_node = current_node.next

  def swap(self, node1, node2):
    node1.data, node2.data = node2.data, node1.data

  def bubble_sort(self):

    current_node = self.head

    while current_node and current_node.next:
        if current_node.data > current_node.next.data:
            self.swap(current_node, current_node.next)
        current_node = current_node.next


third_node = Node(3)
second_node = Node(-2, third_node)
first_node = Node(1, second_node)

linked_list = LinkedList(first_node)

print("Lista original:")
linked_list.print_structure()

linked_list.bubble_sort()

print("Lista ordenada:")
linked_list.print_structure()
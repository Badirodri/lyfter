# 3. Cree una estructura de objetos que asemeje un Binary Tree.
#     1. Debe incluir un método para hacer `print` de toda la estructura.
#     2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive(node.right, value)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root

        if node.right:
            self.print_tree(node.right, level + 1)

        print("    " * level + f"{node.value}")

        if node.left:
            self.print_tree(node.left, level + 1)

tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

tree.print_tree()

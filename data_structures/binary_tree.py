class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = Node()


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.value)
        in_order_traversal(node.right)


# Big O(n)
def pre_order_traversal(node):
    if node is not None:
        print(node.value)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


# Big O(n)
def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value)

# Level order (breadth-first)


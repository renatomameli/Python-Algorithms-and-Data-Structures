from data_structures.binary_tree import BinaryTree, in_order_traversal, Node
from data_structures.linked_list import LinkedList


def linked_list():
    my_list = LinkedList()
    my_list.display()
    my_list.append(0)
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.display()
    my_list.deleteAt(0)
    my_list.display()


def binary_tree():
    my_binary_tree = BinaryTree()
    my_binary_tree.root.value = 3
    my_binary_tree.root.left = Node(3)
    my_binary_tree.root.right = Node(4)
    in_order_traversal(my_binary_tree.root)


if __name__ == '__main__':
    # linked_list()
    binary_tree()

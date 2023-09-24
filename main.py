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


if __name__ == '__main__':
    linked_list()

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        if current == self.head and self.head.data is None:
            current.data = data
        else:
            current.next = new_node

    def length(self):
        count = 0
        current = self.head
        while current.next is not None:
            current = current.next
            count += 1
        return count

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        print(elements)

    def getAt(self, index):
        current = self.head
        for i in range(index):
            if current.next is None:
                raise Exception("Out of bounce exception")
            current = current.next
        return current

    def deleteAt(self, index):
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for i in range(index-1):
            if current.next is None:
                raise Exception("Out of bounce exception")
            current = current.next

        if current.next is None or current.next.next is None:
            raise Exception("Out of bounce exception")
        current.next = current.next.next

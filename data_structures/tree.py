class Node:
    def __init__(self, name=None, children=None):
        if children is None:
            children = []
        self.name = name
        self.children = children


class Tree:
    def __init__(self):
        self.root = Node()


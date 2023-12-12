class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        pushed_node = Node(data)
        pushed_node.next = self.top
        self.top = pushed_node

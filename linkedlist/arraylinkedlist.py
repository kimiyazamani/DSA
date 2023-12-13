class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Array:
    def __init__(self):
        self.head = None

    def append(self, data):
        appended_node = Node(data)
        if self.head is None:
            self.head = appended_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = appended_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            return popped_node.data

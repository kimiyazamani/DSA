class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def InsertAtIndex(self, data, index):
        if index < 0 or index > self.size:
            return

    new_node = Node(data)
    if index == 0:
        if self.head is None:
            self.head = new_node
            new_node.next = new_node  
        else:
            new_node.next = self.head
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            self.head = new_node
    else:
    
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

        self.size += 1

    def InsertAtBegin(self, data):
        self.InsertAtIndex(data, 0)

    def InsertAtEnd(self, data):
        self.InsertAtIndex(data, self.size)

    def UpdateNode(self, data, index):
        if index < 0 or index >= self.size:
            return

        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        cur.data = data

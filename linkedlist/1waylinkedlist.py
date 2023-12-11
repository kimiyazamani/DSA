class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def InsertAtIndex(self, data, index):
        if index < 0 or index > self.size:
            return
        
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
        
        self.size += 1
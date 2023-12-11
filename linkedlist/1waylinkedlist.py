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

    def InsertAtBegin(self, data):
        self.InsertAtIndex(data, 0)

    def InsertAtEnd(self, data):
        self.InsertAtIndex(data, self.size)

    def UpdateNode(self, data, index):
        if index < 0 or index >= self.size:
            return

        cur = self.head
        for _ in range(index):
            cur = cur.next
        cur.data = data

    def RemoveNodeAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            removed_data = self.head.data
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                current = cur.next
            removed_data = cur.next.data
            cur.next = cur.next.next

        self.size -= 1
        return removed_data

    def RemoveNodeAtBegin(self):
        return self.RemoveNodeAtIndex(0)

    def RemoveNodeAtEnd(self):
        return self.RemoveNodeAtIndex(self.size - 1)
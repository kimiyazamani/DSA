class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def InsertAtIndex(self, data, index):
        if index < 0 or index > self.size:
            return

        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            new_node.prev = cur
            new_node.next = cur.next
            cur.next.prev = new_node
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

        if self.size == 1:
            removed_data = self.head.data
            self.head = None
            self.tail = None
        elif index == 0:
            removed_data = self.head.data
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size - 1:
            removed_data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            removed_data = cur.data
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

        self.size -= 1
        return removed_data

    def RemoveNodeAtBegin(self):
        return self.RemoveNodeAtIndex(0)

    def RemoveNodeAtEnd(self):
        return self.RemoveNodeAtIndex(self.size - 1)

    def SizeOfList(self):
        return self.size

    def Concatenate(self, other_list):
        if not isinstance(other_list, DoublyLinkedList):
            return

        if self.size == 0:
            self.head = other_list.head
            self.tail = other_list.tail
        elif other_list.size > 0:
            self.tail.next = other_list.head
            other_list.head.prev = self.tail
            self.tail = other_list.tail

        self.size += other_list.size
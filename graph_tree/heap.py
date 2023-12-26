class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up()
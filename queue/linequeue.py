class Queue:

    def __init__(self):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = 0
        self.rear = 0



    def IsFull(self):
         if (self.size==self.rear):
            return True
    

    def IsEmpty(self):
        if (self.front == self.rear):
            return True
        else:
            return False

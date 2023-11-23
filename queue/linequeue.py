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

    def Enqueue(self, item):
        if self.is_full():
            print("Queue is full.")
           
        else:
            self.queue[self.rear] = data
            self.rear = self.rear + 1

    def Dequeue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            dequeued_item = self.item[self.front]
            self.front += 1
            return dequeued_item

    def Peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.queue[0]

    def ReverseQueue(self):
        if self.is_empty():
            print("The queue is empty!")
            return 
        else:
            f=self.front
            r=(self.rear-1)%self.size
            while i<j:
                self.queue[f],self.queue[r]=self.queue[r],self.queue[f]
                f+=1
                r=1
            return
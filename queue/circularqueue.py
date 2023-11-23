class Queue:

    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=0
        self.rear=0
     
        
    def IsEmpty(self):
        if self.front==self.rear:
            return True
        
    def IsFull(self):
        if ((self.rear+1)%self.size)==self.front:
            return True

    def Enqueue(self,item):  
        if self.is_full():
            print("Queue is full.")
            return
        else:
            self.queue[self.rear]=item
            self.rear=(self.rear+1)%self.size

    def Dequeue(self): 
        if self.is_empty():
            print("Queue is empty.")
            return
        else:
            value=self.queue[self.front]
            self.queue[self.front]=None
            self.front=(self.front+1) % self.size
            return value

    def Peek(self): 
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.queue[self.front]
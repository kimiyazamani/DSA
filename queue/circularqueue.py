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
class QueueUsingStacks:
    
    def __init__(self):
        self.stack1 = []  
        self.stack2 = []  

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2 += [self.stack1[-1]]
                self.stack1 = self.stack1[:-1]

        return self.stack2.pop()
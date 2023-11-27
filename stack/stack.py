class Stack:
    def __init__(self, size):
        self.size = size
        self.List = [None] * size
        self.top = 0

    def is_empty(self):
        if self.top==0:
            return True
        else:
            return False
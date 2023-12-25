class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hasht(self, key):
        return hash(key) % self.size
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hasht(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hasht(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def delete(self, key):
        index = self.hasht(key)
        if self.table[index] is not None:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    break

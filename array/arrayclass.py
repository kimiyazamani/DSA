class Array:
    def __init__(self):
        self.array = []

    def insert(self, obj, index):

        self.array += [None]
        for i in range(len(self.array) - 1, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = obj

    def delete(self, index):
        deleted_object = self.array[index]

        for i in range(index, len(self.array) - 1):
            self.array[i] = self.array[i + 1]

        self.array = self.array[:-1]

        return deleted_object

    def find(self, obj):
       
        for i in range(len(self.array)):
            if self.array[i] == obj:
                return i

        return -1

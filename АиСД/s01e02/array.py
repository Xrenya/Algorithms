class ArrayV1:
    def __init__(self):
        self.array = []
        self.size = 0
        self.min_index = None
        
    def append(self, x):
        if self.min_index is not None and self.array[self.min_index] < x:
            self.min_index = self.size - 1
        self.array.append(x)
        self.size += 1
        
    def insert(self, x, index):
        if self.min_index is not None and self.array[self.min_index] < x:
            self.min_index = index
        if index < 0 or index > self.size:
            raise ValueError("Index out of range")
        array = self.array[:index] + [x] + self.array[index:]
        self.array = array      
        self.size += 1
        
    def get(self, index):
        return self.array[index]

    def get_min(self):
        if self.min_index is not None:
            return self.array[self.min_index]
        self.min_index = 0
        for i in range(self.size):
            if self.array[i] < self.array[self.min_index]:
                self.min_index = i
        return self.array[self.min_index]
        
    def remove_min(self):
        if self.min_index is not None:
            self.array[self.min_index], self.array[self.size - 1] = self.array[self.size - 1], self.array[self.min_index]
            self.size -= 1
            self.min_index = None
            self.get_min()
        else:
            self.get_min()
            self.array[self.min_index], self.array[self.size - 1] = self.array[self.size - 1], self.array[self.min_index]
            self.array = self.array[:self.size - 1]
            self.min_index = None
            self.size -= 1
            self.get_min()
    
    
ar = ArrayV1()
ar.append(1)
ar.append(2)
ar.append(3)
ar.insert(0, 0)
ar.insert(-1, 0)
print(ar.array)
ar.remove_min()
print(ar.array)
print(ar.get_min())

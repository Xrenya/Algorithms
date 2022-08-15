class Heap:
    """Keep descending array in order to have access to a minimum"""
    def __init__(self, array):
        self.array = array
        self.size = len(self.array)
        
    def insert(self, x):
        self.array.append(x)
        self.size += 1
        j = self.size - 1
        while j > 0 and self.array[j] < self.array[(j - 1) // 2]:
            self.array[j], self.array[(j - 1) // 2] = self.array[(j - 1) // 2], self.array[j]
            j = (j - 1) // 2
            
    def remove_min(self):  # O(lg(n))
        self.array[0] = self.array[self.size - 1]
        self.array.pop()
        self.size -= 1
        i = 0
        n = self.size
        while 2 * i + 1 < n:
            j = 2 * i + 1
            if 2 * i + 2 < n and self.array[2 * i + 2] < self.array[j]:
                j = 2 * i + 2
            if self.array[i] <= self.array[j]:
                break
            else:
                self.array[j], self.array[i] = self.array[i], self.array[j]
                i = j

    def get_min(self):
        return self.array[0]

array = [2, 5, 7, 8, 6, 10, 42, 11, 15, 28, 9, 13]
heap = Heap(array)
heap.insert(4)
print(heap.array)  # [2, 5, 4, 8, 6, 7, 42, 11, 15, 28, 9, 13, 10]
print(heap.get_min())  # 2
heap.insert(0)
print(heap.get_min())  # 0

array = [1, 5, 4]
print(array)
heap = Heap(array)
heap.insert(10)
print(heap.array)  # [1, 5, 4, 10]
heap.remove_min()
print(heap.array)  # [4, 5, 10]

class Heap:
    """Keep descending array in order to have access to a minimum"""
    def __init__(self, array):
        self.array = array
        self.size = len(self.array)
        
    def insert(self, x):
        self.array.append(x)
        self.size += 1
        j = self.size - 1
        while j > 0 and self.array[j] > self.array[(j - 1) // 2]:
            self.array[j], self.array[(j - 1) // 2] = self.array[(j - 1) // 2], self.array[j]
            j = (j - 1) // 2
            
    def remove_max(self):  # O(lg(n))
        self.array[0] = self.array[self.size - 1]
        self.array.pop()
        self.size -= 1
        i = 0
        n = self.size
        while 2 * i + 1 < n:
            j = 2 * i + 1
            if 2 * i + 2 < n and self.array[2 * i + 2] > self.array[j]:
                j = 2 * i + 2
            if self.array[i] >= self.array[j]:
                break
            else:
                self.array[j], self.array[i] = self.array[i], self.array[j]
                i = j

    def get_min(self):
        return self.array[0]
        
    def sort(self):
        output = []
        n = self.size
        for _ in range(n):
            output.append(self.get_min())
            self.remove_max()
        return output
        
    def heapify(self):
        for i in range(self.size):
            self.sift_up(i)
        
    def sift_up(self, j):
        while j > 0 and self.array[j] > self.array[(j - 1) // 2]:
            self.array[j], self.array[(j - 1) // 2] = self.array[(j - 1) // 2], self.array[j]
            j = (j - 1) // 2
            
        

array = [2, 3, 4, 5]
heap = Heap(array)
print(heap.array)  # [5, 4, 3, 2]
heap.heapify()
print(heap.array)  # [5, 4, 3, 2]
print(heap.sort())  # [5, 4, 3, 2]

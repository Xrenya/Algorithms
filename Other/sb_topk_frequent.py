# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

class Heap:
    def __init__(self):
        self.array = []
        self.size = 0
        
    def insert(self, val, count):
        self.array.append((val, count))
        i = self.size
        self.size += 1
        while i > 0 and self.array[i][1] > self.array[(i - 1) // 2][1]:
            self.array[i], self.array[(i - 1) // 2] = self.array[(i - 1) // 2], self.array[i]
            i = (i - 1) // 2
            
    def pop(self):
        self.array[0], self.array[self.size - 1] = self.array[self.size - 1], self.array[0]
        largest = self.array.pop()
        self.size -= 1
        i = 0
        while 2 * i + 1 < self.size and self.array[2 * i + 1][1] > self.array[i][1]:
            j = 2 * i + 1
            if 2 * i + 2 < self.size and self.array[2 * i + 1][1] < self.array[2 * i + 2][1]:
                j = 2 * i + 2
            if self.array[j][1] < self.array[i][1]:
                break
            self.array[i], self.array[j] = self.array[j], self.array[i]
            i = j
        return largest[0]
        
        
heap = Heap()

for v, c in [(0, 10), (10, 1), (9, 2), (-1, 7)]:
    heap.insert(v, c)
    
for _ in range(3):
    print(heap.pop())





NUM_BUCKETS = 2003 # A prime number

class MyHashSet:

    def __init__(self):
        # Make the hash buckets.
        self.buckets = [[] for _ in range(NUM_BUCKETS)]

    def add(self, key: int) -> None:
        mod = key % NUM_BUCKETS
        if not key in self.buckets[mod]:
            self.buckets[mod].append(key)

    def remove(self, key: int) -> None:
        mod = key % NUM_BUCKETS
        # Remove if it's present
        try:
            self.buckets[mod].remove(key)
        except:
            pass
           
    def contains(self, key: int) -> bool:
        mod = key % NUM_BUCKETS
        return key in self.buckets[mod]
      
      
class MyHashSet:

    def __init__(self):
        self.array = []
        self.index = 0
        self.dict = {}

    def add(self, key: int) -> None:
        self.array.append(key)
        self.dict[key] = self.index
        self.index += 1
        

    def remove(self, key: int) -> None:
        if key in self.dict:
            cur_index = self.dict[key]
            temp = self.array[len(self.array) - 1]
            self.array[len(self.array) - 1] = key
            self.array[cur_index] = temp
            self.dict[temp] = cur_index
            del self.dict[key]
            self.array.pop()
            self.index -= 1
            

    def contains(self, key: int) -> bool:
        if key in self.dict:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

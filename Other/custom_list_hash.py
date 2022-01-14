# insert(10)
# insert(20)
# insert(30)
# sample() -> 20
# sample() -> 20
# sample() -> 30


import random_int(a, b)


class HashList:
    def __init__(self):
        self.sample_array = []
        self.index_hash = defaultdict(int)
        # self.index = 0
    
    def insert(self, x):
        self.index_hash[x] = len(self.sample_array)
        self.sample_array.append(x)
    
    def contains(self, x):        
        # flag = self.index_hash.get(x, False)
        return True if x in self.index_hash  else False
       
    def remove(self, x):
        swap_index = self.index_hash[x]
        last = len(self.sample_array) - 1
        last_num = self.sample_array[-1]
        self.sample_array[swap_index], self.sample_array[last] = self.sample_array[last], self.sample_array[swap_index] 
        self.index_hash[last_num] = swap_index
        self.index_hash.remove(x)
        self.sample_array.pop()
    
    def sample(self):
        index = random_int(0, len(self.sample_array) - 1)
        return self.sample_array[index]
    
    
# insert(10) -> [10] -> 1 -> pop()
# remove(10)
# [], {}

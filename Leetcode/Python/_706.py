class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for i, (k, v) in enumerate(self.bucket):
            if key == k:
                return v
        return -1

    def update(self, key, value):
        exist = False
        for i, (k, v) in enumerate(self.bucket):
            if key == k:
                self.bucket[i] = (key, value)
                exist = True
                break
        if not exist:
            self.bucket.append((key, value))

    def remove(self, key):
        remove = -1
        for i, (k, v) in enumerate(self.bucket):
            if key == k:
                remove = i
                break
        if remove != -1:
            self.bucket[remove], self.bucket[len(self.bucket) - 1] = self.bucket[len(self.bucket) - 1],  self.bucket[remove]
            self.bucket.pop()


class MyHashMap:
    def __init__(self):
        self.key = 2069
        self.hash = [Bucket() for _ in range(self.key)]
        
    def put(self, key, value):
        hash_key = key % self.key
        self.hash[hash_key].update(key, value)
        
    def get(self, key):
        hash_key = key % self.key
        return self.hash[hash_key].get(key)
    
    def remove(self, key):
        hash_key = key % self.key
        self.hash[hash_key].remove(key)

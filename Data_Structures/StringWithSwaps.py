class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        num_nodes = len(s)
        self.uf = UnionFind(num_nodes)
        for i,j in pairs:
            self.uf.union(i,j)

        indexes_by_root = {}
        chars_by_root = {}
        for i in range(num_nodes):
            root = self.uf.find(i)
            if root not in indexes_by_root:
                indexes_by_root[root] = [i]
                chars_by_root[root] = [s[i]]
            else:
                indexes_by_root[root].append(i)
                chars_by_root[root].append(s[i])
            print(indexes_by_root, chars_by_root)
        
        result = [None] * num_nodes
        for root in indexes_by_root:
            sorted_characters = sorted(chars_by_root[root])
            for index, slot in enumerate(indexes_by_root[root]):
                result[slot] = sorted_characters[index]
        result = ''.join(result)
        return result

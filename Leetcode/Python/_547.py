class UnionFind:
    def __init__(self, n):
        self.list = [i for i in range(n)]

    def find(self, x):
        return self.list[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.list)):
                if self.list[i] == root_y:
                    self.list[i] = root_x

    def connected(self, x, y):
        return self.list[x] == self.list[y]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        union_fold = UnionFind(n)

        for u in range(n):
            for v in range(n):
                if u != v and isConnected[u][v] == 1:
                    union_fold.union(u, v)
        return len(set(union_fold.list))

class Union(object):
    def __init__(self, size: int):
        self.size = size
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        union = Union(n)
        for i in range(n):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    union.union(i, j)
        for i in range(len(isConnected)):
            union.find(i)
            
        return len(list(set(union.root))) 

        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(row):
            visited.add(row)
            for col in range(len(isConnected)):
                if isConnected[row][col] == 1 and col not in visited:
                    visited.add(col)
                    dfs(col)
        count = 0
        visited = set()
        for row in range(len(isConnected)):
            if row not in visited:
                dfs(row)
                count += 1
        return count

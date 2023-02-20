class UnionFind:
    """
    Standard Union-Find by Rank with Path Compression
    """
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        
        return self.parents[i]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b: return False
        
        # Union by rank
        if self.rank[root_a] < self.rank[root_b]:
            self.parents[root_a] = self.parents[root_b]
        elif self.rank[root_b] < self.rank[root_a]:
            self.parents[root_b] = root_a
        else:
            self.parents[root_b] = root_a
            self.rank[root_a] += 1
        return True
    
    def copy(self):
        uf = UnionFind(0)
        uf.parents = self.parents.copy()
        uf.rank = self.rank.copy()
        return uf
        

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # not enough edges
        if len(edges) < n - 1: return -1
        
        aliceUF = UnionFind(n + 1)
        aEdges = bEdges = ans = 0
        
        # 1) connect all type 3 edges, discarding edges that join two edges in the same set
        for type, start, end in edges:
            if type == 3:
                if aliceUF.union(start, end):
                    aEdges += 1
                    bEdges += 1
                else:
                    ans += 1
        
        # 2) remove edges for each individual that connect the same set
        
        # copy the Union-Find DS for Bob (already contains the type 3 edges)
        bobUF = aliceUF.copy()
        for type, start, end in edges:
            # Alice
            if type == 1:
                if aliceUF.union(start, end):
                    aEdges += 1
                else:
                    ans += 1
            
            # Bob
            elif type == 2:
                if bobUF.union(start, end):
                    bEdges += 1
                else:
                    ans += 1
        
        # Fully connected if each person has exactly n - 1 edges
        return ans if aEdges == bEdges == n - 1 else -1

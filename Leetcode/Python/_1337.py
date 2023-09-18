import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        def binsearch(row):
            left = -1
            right = len(row)
            while left < right - 1:
                m = left + (right - left) // 2
                if row[m] == 1:
                    left = m
                else:
                    right = m
            return right

        q = []
        for i, row in enumerate(mat):
            strenght = binsearch(row)
            key = (-strenght, -i)
            if len(q) < k or key > q[0]:
                heapq.heappush(q, key)
            if len(q) > k:
                heapq.heappop(q)

        indexes = []
        while q:
            s, i = heapq.heappop(q)
            indexes.append(-i)
        
        return indexes[::-1]

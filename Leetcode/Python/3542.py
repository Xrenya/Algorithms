class Solution:
    def minOperations(self, nums: List[int]) -> int:
        q = []
        ops = 0
        for n in nums:
            while q and q[-1] > n:
                q.pop()
            if n == 0:
                continue
            if not q or q[-1] < n:
                ops += 1
                q.append(n)
        return ops

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def counter(index, acc):
            if index == n:
                return acc == target
            
            if (index, acc) in memo:
                return memo[(index, acc)]
            
            count = 0
            for i in range(1, min(k, target - acc) + 1):
                count = (count + counter(index + 1, i + acc)) % MOD
            memo[(index, acc)] = count
            return count
        memo = {}
        MOD = 10**9 + 7
        return counter(0, 0)

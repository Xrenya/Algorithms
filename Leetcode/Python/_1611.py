class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        k = 0
        cur = 1
        while (cur * 2) <= n:
            cur *= 2
            k += 1

        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(n ^ cur)

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        dist = 0
        mask = 1
        while xor:
            dist += (mask & xor)
            xor >>= 1
        return dist

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Time complexity O(n)
        output = 0
        for string in stones:
            if string in jewels:
                output += 1
        return output

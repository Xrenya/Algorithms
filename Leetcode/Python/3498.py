class Solution:
    def reverseDegree(self, s: str) -> int:
        output = 0
        for i, char in enumerate(s):
            val = 26 - (ord(char) - ord('a'))
            output += val * (i + 1)
        return output

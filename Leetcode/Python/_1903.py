class Solution:
    def largestOddNumber(self, num: str) -> str:
        cur = ""
        for right in range(len(num)):
            if int(num[right]) % 2:
                cur = num[:right + 1]
        return cur

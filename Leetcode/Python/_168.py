class Solution:
    def convertToTitle(self, n: int) -> str:
        string = ""
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            string = chr(65 + remainder) + string
        return string

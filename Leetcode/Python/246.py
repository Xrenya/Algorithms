class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        output = ""
        mapping = {"9": "6", "6": "9", "0": "0", "1": "1", "8": "8"}
        for n in num[::-1]:
            if n not in mapping:
                return False
            output += mapping[n]
        return output == num

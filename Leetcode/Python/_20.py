class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        hashMap = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in hashMap:
                temp.append(hashMap[c])
            elif len(temp) > 0 and c == temp[-1]:
                temp.pop()
            else:
                return False
        return len(temp) == 0

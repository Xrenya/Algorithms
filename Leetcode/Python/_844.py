class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.deletor(s)
        t = self.deletor(t)
        return s == t

    def deletor(self, s):
        s1 = ""
        skip = 0
        for i in range(len(s)):
            if skip != 0 and s[len(s) - 1 - i] != "#":
                skip -= 1
            elif s[len(s) - 1 - i] == "#":
                skip += 1
            else:
                s1 = s1 + s[len(s) - 1 - i]
        return s1
            

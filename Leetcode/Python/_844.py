class Solution:
    def get_current_index(self, s, i):
        to_skip = 0
        while i >= 0:
            if s[i] == "#":
                to_skip += 1
            elif to_skip > 0:
                to_skip -= 1
            else:
                break
            i -= 1
        return i
        
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        while i >= 0 or j >= 0:
            i = self.get_current_index(s, i)
            j = self.get_current_index(t, j)
            
            if i < 0 and j < 0:
                return True
            
            if i < 0 or j < 0:
                return False
            
            if s[i] != t[j]:
                return False
            
            i -= 1
            j -= 1
            
        return True

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
            

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = self.dict(s)
        t = self.dict(t)
        if len(s) != len(t):
            return False
        else:
            for key, val in s.items():
                value = t.get(key, False)
                if value:
                    if value != val:
                        return False
                else:
                    return False
        return True
        
        
    def dict(self, s):
        hashMap = {}
        for string in s:
            if string not in hashMap:
                hashMap[string] = 0
            hashMap[string] +=1
        return hashMap 

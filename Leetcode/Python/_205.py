class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        self.s2t = {}
        self.t2s = {}

        for i in range(len(s)):
            if s[i] not in self.s2t and t[i] not in self.t2s:
                self.s2t[s[i]] = t[i]
                self.t2s[t[i]] = s[i]
            elif (s[i] in self.s2t and t[i] not in self.t2s) or (s[i] not in self.s2t and t[i] in self.t2s):
                return False
            if not self.s2t[s[i]] == t[i] and not self.t2s[t[i]] == s[i]:
                return False
        return True

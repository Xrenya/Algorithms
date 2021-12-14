class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.result = []
        self.travers("", s, 0)
        return self.result
    
    def travers(self, current, s, i):
        if len(current) == len(s):
            self.result.append(current)
            return
        
        self.travers(current + s[i], s, i + 1)
        if s[i].isalpha():
            self.travers(current + s[i].swapcase(), s, i + 1)
        return

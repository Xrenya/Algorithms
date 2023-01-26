class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [[]]

        for char in s:
            n = len(output)
            if char.isalpha():
                for i in range(n):
                    output.append(output[i][:])
                    output[i].append(char.lower())
                    output[n + i].append(char.upper())
            else:
                for i in range(n):
                    output[i].append(char)

        return map("".join, output)

    
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

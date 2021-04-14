class Solution:
    def removeDuplicates(self, S: str) -> str:
        array = []
        for s in S:
            if len(array) == 0:
                array.append(s)
            else:
                if s == array[-1]:
                    array.pop()
                else:
                    array.append(s)
        return ''.join(array)

class Solution:
    def removeDuplicates(self, S: str) -> str:
        string = ''
        for s in S:
            if len(string) == 0:
                string += s
            else:
                if s == string[-1]:
                    string = string[:len(string)-1]
                else:
                    string += s
        return string
      
class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        S = list(S)
        while i < len(S) - 1:
            if S[i] == S[i+1]:
                del S[i]
                del S[i]
                if i:
                    i -= 1
            else:
                i += 1
        return ''.join

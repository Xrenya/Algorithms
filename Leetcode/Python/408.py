class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        stack = []
        tmp = 0
        for c in abbr:
            if c.isdigit():
                if tmp == 0 and int(c) == 0:
                    return False
                tmp = tmp * 10 + int(c)
            else:
                if tmp > 0:
                    stack.append(tmp)
                    tmp = 0
                stack.append(c)
        if tmp > 0:
            stack.append(tmp)
        j = 0
        i = 0
        while i < len(word):
            if j == len(stack):
                return False
            elif isinstance(stack[j], int):
                i += stack[j]
                j += 1
            elif word[i] != stack[j]:
                return False
            else:
                i += 1
                j += 1

        return i == len(word) and j == len(stack)
            
            

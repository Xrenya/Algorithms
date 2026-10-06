class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        closed = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    closed += 1
        return len(stack) + closed

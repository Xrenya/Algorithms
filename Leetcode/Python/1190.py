class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = list(s)
        def dfs(start, end):
            if end == len(s):
                return
            
            if ")" == s[end]:
                st = start.pop()
                stack[st + 1:end] = stack[st + 1:end][::-1]
            elif s[end] == "(":
                start.append(end)
            dfs(start, end + 1)
        dfs([], 0)
        output = ""
        for c in stack:
            if c not in ("(", ")"):
                output += c
        return output

    def reverseParenthesesV2(self, s: str) -> str:
        starts = []
        output = []
        index = 0
        for i, c in enumerate(s):
            if c == "(":
                starts.append(index)
            elif c == ")":
                start = starts.pop()
                output[start:] = output[start:][::-1]
            else:
                index += 1
                output.append(c)
        return ''.join(output)

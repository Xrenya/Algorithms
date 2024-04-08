class Solution:
    def checkValidString(self, s: str) -> bool:
        open_brackets = []
        ast = []

        for i, c in enumerate(s):
            if c == "(":
                open_brackets.append(i)
            elif c == "*":
                ast.append(i)
            else:
                if open_brackets:
                    open_brackets.pop()
                elif ast:
                    ast.pop()
                else:
                    return False
        while open_brackets and ast:
            if open_brackets.pop() > ast.pop():
                return False

        return not open_brackets

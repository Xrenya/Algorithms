class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        self.valid = set()
        self.removed = len(s) + 1

        @cache
        def dfs(index, opened, closed, removed, cur):
            if index == len(s):
                if opened == closed:
                    if removed < self.removed:
                        self.valid = {cur,}
                        self.removed = removed
                    elif removed == self.removed:
                        self.valid.add(cur)
            else:
                if s[index] != '(' and s[index] != ')':
                    dfs(index + 1, opened, closed, removed, cur + s[index])
                else:
                    dfs(index + 1, opened, closed, removed + 1, cur)
                    if s[index] == '(':
                        dfs(index + 1, opened + 1, closed, removed, cur + s[index])
                    elif opened > closed:
                        dfs(index + 1, opened, closed + 1, removed, cur + s[index])

        dfs(0, 0, 0, 0, "")
        return list(self.valid)

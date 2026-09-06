class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i, j):
            if j == len(t) or i == len(s):
                return int(j == len(t))

            if (i, j) in memo:
                return memo[(i, j)]

            output = dfs(i + 1, j)

            if s[i] == t[j]:
                output += dfs(i + 1, j + 1)
            memo[(i, j)] = output
            return output

        memo = {}
        return dfs(0, 0)

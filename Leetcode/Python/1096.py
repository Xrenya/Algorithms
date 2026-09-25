class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        output = set()

        def dfs(exp):
            r = exp.find("}")

            if r == -1:
                output.add(exp)
                return

            l = exp.rfind("{", 0, r)

            left = exp[:l]
            right = exp[r + 1:]

            inside = exp[l + 1:r]
            for part in inside.split(","):
                dfs(left + part + right)


        dfs(expression)
        return sorted(output)

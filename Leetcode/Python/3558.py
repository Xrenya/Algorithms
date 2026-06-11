from typing import List

class Solution:
    MOD = 10**9 + 7

    def dfs(self, g: List[List[int]], x: int, f: int):
        max_dep: int = 0
        for y in g[x]:
            if y == f:
                continue
            max_dep = max(max_dep, self.dfs(g, y, x) + 1)
        return max_dep

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n: int = len(edges) + 1
        g: List[List[int]] = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        max_dep = self.dfs(g, 1, 0)
        return pow(2, max_dep - 1, self.MOD)

expectedOutput: int = 1
output: int = Solution().assignEdgeWeights([[1,2]])
assert (expectedOutput == output), (
    f"`output` is not correct, expected '{expectedOutput}', but "
    f"got f'{output}'")

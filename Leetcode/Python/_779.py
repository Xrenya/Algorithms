class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(n, k, node):
            if n == 1:
                return node
            total_nodes = 2 ** (n - 1)
            if k > total_nodes // 2:
                node = 1 if node == 0 else 0
                return dfs(n - 1, k - total_nodes // 2, node)
            else:
                node = 0 if node == 0 else 1
                return dfs(n - 1, k, node)
        return dfs(n, k, 0)

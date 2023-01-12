class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node):
            counter = Counter(labels[node])
            visited.add(node)
            for cur in adj[node]:
                if cur in visited:
                    continue
                counter += dfs(cur)
            output[node] = counter[labels[node]]
            return counter

        output = [0] * n
        visited = set()
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dfs(0)
        return output

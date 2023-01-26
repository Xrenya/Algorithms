class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if  len(connections) < n - 1:
            return -1

        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            for cur_node in graph[node]:
                dfs(cur_node)
            return 1

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        count = 0
        for node in range(n):
            if dfs(node):
                count += 1

        return count - 1

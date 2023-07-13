class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n

        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

            
        safe_nodes = []
        for i in range(n):
            if safe[i]:
                safe_nodes.append(i)

        return safe_nodes


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        safe = [False] * N

        graph = [set(neighbors) for neighbors in graph]
        rgraph = [set() for _ in range(N)]
        q = collections.deque()

        for i, js in enumerate(graph):
            if not js:
                q.append(i)
            for j in js:
                rgraph[j].add(i)

        while q:
            j = q.popleft()
            safe[j] = True
            for i in rgraph[j]:
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    q.append(i)

        return [i for i, is_safe in enumerate(safe) if is_safe]

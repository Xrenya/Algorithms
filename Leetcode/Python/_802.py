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

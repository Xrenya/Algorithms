class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(source):
            q = deque([source])
            color[source] = 0
            while q:
                node = q.popleft()
                for neighbour in adj[node]:
                    if color[neighbour] == color[node]:
                        return False
                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[node]
                        q.append(neighbour)

            return True
        
        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        color = [-1] * (n + 1)
        for i in range(1, n + 1):
            if color[i] == -1:
                if not bfs(i):
                    return False

        return True

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        mapping = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1, y1, r1 = bombs[i]
                x2, y2, _ = bombs[j]

                if (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r1 ** 2:
                    mapping[i].append(j)

        def bfs(node):
            visited = set()
            queue = deque([node])
            while queue:
                bomb = queue.popleft()
                visited.add(bomb)
                for neighbour in mapping[bomb]:
                    if neighbour not in visited:
                        queue.append(neighbour)
            return len(visited)

        def dfs(node, visited):
            visited.add(node)
            for neighbour in mapping[node]:
                if neighbour not in visited:
                    dfs(neighbour, visited)

        maximum = 0
        for i in range(n):
            visited = set()
            dfs(i, visited)
            maximum = max(maximum, len(visited))

        return maximum

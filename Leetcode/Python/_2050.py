class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n
        graph = defaultdict(list)

        for in_, out_ in relations:
            graph[in_ - 1].append(out_ - 1)
            indegree[out_ - 1] += 1

        queue = deque()
        max_time = [0] * n
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                max_time[i] = time[i]

        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                max_time[neighbour] = max(max_time[neighbour], max_time[node] + time[neighbour])
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return max(max_time)

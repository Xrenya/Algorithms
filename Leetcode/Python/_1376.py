class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        queue = collections.deque([(headID, 0)])

        graph = collections.defaultdict(list)
        for i, v in enumerate(manager):
            graph[v].append(i)
        
        ans = -1
        while queue:
            empID, time = queue.popleft()
            ans = max(ans, time)

            for adj in graph[empID]:
                queue.append((adj, time + informTime[empID]))
        return ans

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        queue = deque([start])
        visited = set()
        n = len(arr)
        while queue:
            node = queue.popleft()
            visited.add(node)
            for next_node in (node - arr[node], node + arr[node]):
                if 0 <= next_node < n and next_node not in visited:
                    if arr[next_node] == 0:
                        return True
                    queue.append(next_node)
        return False

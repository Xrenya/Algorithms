class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        d1 = [float("inf") for _ in range(n)]
        d2 = [float("inf") for _ in range(n)]
        def bfs(node, dist):
            visited = set([node])
            queue = deque([(node, 0)])
            while queue:
                cur_node, cur_dist = queue.popleft()
                dist[cur_node] = cur_dist
                if edges[cur_node] != -1 and edges[cur_node] not in visited:
                    visited.add(edges[cur_node])
                    queue.append((edges[cur_node], cur_dist + 1))
            return
        
        bfs(node1, d1)
        bfs(node2, d2)
        cur_min = float("inf")
        output_node = -1
        for node in range(n):
            dist = max(d1[node], d2[node])
            if cur_min > dist:
                cur_min = dist
                output_node = node
                
        return output_node
            

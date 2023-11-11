class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = [[] for _ in range(n)]
        for from_node, to_node, cost in edges:
            self.adj[from_node].append((to_node, cost))

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.adj[from_node].append((to_node, cost))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.adj)
        cost_to_node = [float("inf")] * n
        cost_to_node[node1] = 0
        pq = [(0, node1)]
        while pq:
            cur_cost, cur_node = heappop(pq)
            if cur_cost > cost_to_node[cur_node]:
                continue
            if cur_node == node2:
                return cur_cost
            for nei, cost in self.adj[cur_node]:
                new_cost = cost + cur_cost
                if new_cost < cost_to_node[nei]:
                    cost_to_node[nei] = new_cost
                    heappush(pq, (new_cost, nei))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

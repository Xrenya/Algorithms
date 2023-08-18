class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        rank = 0
        adj = defaultdict(set)
        for road in roads:
            adj[road[0]].add(road[1])
            adj[road[1]].add(road[0])

        for node_1 in range(n):
            for node_2 in range(node_1 + 1, n):
                cur_rank = len(adj[node_1]) + len(adj[node_2])
                if node_1 in adj[node_2]:
                    cur_rank -= 1
                rank = max(rank, cur_rank)
        return rank

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        adj = defaultdict(set)
        for route, stops in enumerate(routes):
            for stop in stops:
                adj[stop].add(route)
        visited = set()
        queue = [(source, 0)]
        for stop, buses in queue:
            if stop == target:
                return buses
            
            for route in adj[stop]:
                for nei in routes[route]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, buses + 1))
                routes[route] = []
        return -1

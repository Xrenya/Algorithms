class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        # building undirected graph
        for s, e in connections:
            graph[s].append((e, True))
            graph[e].append((s, False))
        
        def dfs(currCity):
            count = 0
            if currCity in visited:
                return
            visited.add(currCity)
            for neigh, orig in graph[currCity]:
                if neigh not in visited:
					# if current path is same as original path that were given from input, 
					# we know that we need to invert the path
                    if orig == True:
                        count += 1
                    count += dfs(neigh)
            return count
			
        return dfs(0)

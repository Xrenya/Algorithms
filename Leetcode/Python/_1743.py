class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        root = None
        for node in graph:
            if len(graph[node]) == 1:
                root = node
                break
                
        def dfs(node, prev, output):
            output.append(node)
            for nei in graph[node]:
                if nei != prev:
                    dfs(nei, node, output)
                    
        output = []
        dfs(root, None, output)
        return output

class Solution:
    def dfs(self, adj, start, end, visited = None):
        if visited is None:
            visited = set()
            
        for node in adj[start]:
            if node not in visited:
                visited.add(node)
                if node == end or self.dfs(adj, node, end, visited):
                    return True
        return False
    
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        #edge cases
        if start == end:
            return True
        
        #1. build adjacency list
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # dfs using recursion
        return self.dfs(adj, start, end)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        adjacency_list = [[] for _ in range(n)]
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        
        stack = [start]
        seen = set()
        
        while stack:
            # Get the current node.
            node = stack.pop()
            
            # Check if we have reached the target node.
            if node == end:
                return True
            
            # Check if we've already visited this node.
            if node in seen:
                continue
            seen.add(node)
            
            # Add all neighbors to the stack.
            for neighbor in adjacency_list[node]:
                stack.append(neighbor)
        
        # Our stack is empty and we did not reach the end node.
        return False

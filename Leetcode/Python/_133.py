"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node, mapping):
            if not node:
                return None
            new_node = Node(node.val)
            mapping[node] = new_node
            for nei in node.neighbors:
                if nei not in mapping:
                    new_nei = dfs(nei, mapping)
                new_node.neighbors.append(mapping[nei])
            return new_node
            
        return dfs(node, {})

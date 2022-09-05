"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return  []
        
        output = []
        prev_layer = [root]
        
        while prev_layer:
            cur_layer = []
            output.append([])
            for node in prev_layer:
                output[-1].append(node.val)
                cur_layer.extend(node.children)
                
            prev_layer = cur_layer
        return output
      
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        output = []
        while queue:
            length = len(queue)
            output.append([])
            for _ in range(length):
                node = queue.popleft()
                output[-1].append(node.val)
                queue.extend(node.children)
        return output

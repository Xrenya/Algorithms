# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 1
        
        q = deque([root])
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if not node.left and not node.right:
                    return depth
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            depth += 1
    
        return depth


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.min_depth = float("inf")
        def dfs(node, depth):
            if node:
                depth += 1
                if node.left is None and node.right is None:
                    self.min_depth = min(self.min_depth, depth)
                if node.left:
                    dfs(node.left, depth)
                if node.right:
                    dfs(node.right, depth)
                    
        dfs(root, 0)
        return self.min_depth

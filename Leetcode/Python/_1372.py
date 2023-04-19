# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, left: bool = True, steps: int = 0):
            if node:
                self.length_path = max(self.length_path, steps) 
                if left:
                    dfs(node.right, False, steps + 1)
                    dfs(node.left, True, 1)
                else:
                    dfs(node.left, True, steps + 1)
                    dfs(node.right, False, 1)
                    
                    
        self.length_path = 0
        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.length_path

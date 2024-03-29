# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def lp(node):
            if not node:
                return 0
            
            left = lp(node.left)
            right = lp(node.right)
            
            
            self.diameter = max(self.diameter, left + right)
            
            return max(left, right) + 1
        
        lp(root)
        
        return self.diameter

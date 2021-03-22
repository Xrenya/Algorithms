# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root: return 0
        
        count = 0
        
        if root.val >= low and root.val <= high:
            count += root.val
        
        if root.val > low:
            count += self.rangeSumBST(root.left, low, high)
        
        if root.val < high:
            count += self.rangeSumBST(root.right, low, high)
        
        return count

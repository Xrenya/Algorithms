# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse_and_check(node, min_val, max_val):
            if node is None:
                return True
            if node.val <= min_val or max_val <= node.val:
                return False
            return traverse_and_check(node.left, min_val, node.val) and traverse_and_check(node.right, node.val, max_val)

        
        return traverse_and_check(root, float("-Inf"), float("Inf"))

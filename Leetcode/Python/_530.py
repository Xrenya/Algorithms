# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def get_value_inorder(node):
            if node:
                yield from get_value_inorder(node.left)
                yield node.val
                yield from get_value_inorder(node.right)

        dif = float("inf")
        cur_digit = None
        for val in get_value_inorder(root):
            if cur_digit is not None:
                dif = min(dif, abs(cur_digit - val))
                cur_digit = val
            else:
                cur_digit = val
        return dif

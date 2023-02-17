# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        prev = None
        min_dist = float("inf")
        for node in inorder(root):
            if prev is None:
                prev = node
            else:
                min_dist = min(min_dist, node - prev)
                prev = node

        return min_dist

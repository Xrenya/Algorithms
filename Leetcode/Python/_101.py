# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recusvice_call(node_1, node_2):
            if node_1 is None and node_2 is None:
                return True
            elif node_1 is None or node_2 is None:
                return False
            return node_1.val == node_2.val and recusvice_call(node_1.left, node_2.right) and recusvice_call(node_1.right, node_2.left)
        return recusvice_call(root, root)

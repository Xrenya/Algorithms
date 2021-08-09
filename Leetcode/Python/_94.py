# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        def iot(root):
            if root:
                iot(root.left)
                output.append(root.val)
                iot(root.right)
            
        iot(root)
        return output

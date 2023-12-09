# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        return [x for x in inorder(root

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

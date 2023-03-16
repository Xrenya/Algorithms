# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return None

            val = postorder.pop()
            node = TreeNode(val)

            left_index = mapping_inorder[val]
            node.right = build(left_index + 1, right)
            node.left = build(left, left_index - 1)
            return node


        mapping_inorder = {val: i for i, val in enumerate(inorder)}
        return build(0, len(inorder) - 1)

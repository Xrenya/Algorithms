# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
                
        def parse(nums):
            n = len(nums)
            x = y = None
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x is None:
                        x = nums[i]
            return x, y
        
        def recover(node, couter=2):
            if node:
                if node.val == x or node.val == y:
                    node.val = y if node.val == x else x
                    couter -= 1
                if couter == 0:
                    return
                recover(node.left, couter)
                recover(node.right, couter)
                
        
        nums = [x for x in inorder(root)]
        x, y = parse(nums)
        recover(root, 2)

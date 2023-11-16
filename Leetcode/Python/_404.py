# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left):
          if is_left and not node.left and not node.right:
            self.count += node.val
          if node.left:
            dfs(node.left, True)
          if node.right:
            dfs(node.right, False)
          return
        self.count = 0
        dfs(root, False)
        return self.count


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif root.left and not root.left.left and not root.left.right:
            return root.left.val+self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)

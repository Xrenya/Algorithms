# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.col_index_table = {}
        self.max_width = 0
        def dfs(node: Optional[TreeNode], depth: int, col_index: int):
            if not node:
                return
            if depth not in self.col_index_table:
                self.col_index_table[depth] = col_index

            self.max_width = max(self.max_width, col_index - self.col_index_table[depth] + 1)

            # preorder
            dfs(node.left, depth + 1, 2 * col_index)
            dfs(node.right, depth + 1, 2 * col_index + 1)

        if not root:
            return 0
        dfs(root, 0, 0)
        return self.max_width

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0, 0)
            left_sum, left_count, left_total = dfs(node.left)
            right_sum, right_count, right_total = dfs(node.right)

            acc = left_sum + right_sum + node.val
            count = left_count + right_count + 1
            total_matches = left_total + right_total
            if acc // count == node.val:
                return (acc, count, total_matches + 1)
            return (acc, count, total_matches)

        _, _, matches = dfs(root)
        return matches

    def averageOfSubtreeV2(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            mean = (left[0] + right[0] + node.val) // (left[1] + right[1] + 1)
            if node.val == mean:
                self.count += 1
            return (left[0] + right[0] + node.val), (left[1] + right[1] + 1)
        self.count = 0
        dfs(root)
        return self.count

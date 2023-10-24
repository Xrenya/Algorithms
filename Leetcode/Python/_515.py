# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        rows_values = []
        if not root:
            return rows_values
        queue = deque([root])
        while queue:
            n = len(queue)
            max_rows = -float("inf")
            for _ in range(n):
                node = queue.popleft()
                max_rows = max(max_rows, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rows_values.append(max_rows)
        return rows_values

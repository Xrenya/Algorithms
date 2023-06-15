# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        output = -float("inf")
        level = 0
        output_level = 0
        while queue:
            iters = len(queue)
            acc = 0
            level += 1
            for _ in range(iters):
                node = queue.popleft()
                acc += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if output < acc:
                output = acc
                output_level = level

        return output_level

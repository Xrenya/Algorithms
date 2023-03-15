# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = deque([root])
        null_found = False
        while stack:
            level_len = len(stack)
            for _ in range(level_len):
                node = stack.popleft()
                if node.left:
                    if null_found:
                        return False
                    stack.append(node.left)
                else:
                    null_found = True
                if node.right:
                    if null_found:
                        return False
                    stack.append(node.right)
                else:
                    null_found = True
        return True

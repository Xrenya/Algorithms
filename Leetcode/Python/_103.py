# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        output = []
        queue = deque([root])
        left = True
        while queue:
            nodes = len(queue)
            level = []
            for _ in range(nodes):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if left:
                output.append(level)
                left = False
            else:
                output.append(level[::-1])
                left = True
        
        return output

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = [(root)]
        output = []
        while queue:
            cur = []
            n = len(queue)
            last = None
            for node in queue:
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
                last = node.val
            output.append(last)
            queue = cur
        return output

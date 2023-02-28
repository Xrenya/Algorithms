# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(node):
            if not node:
                return ""
            represantation = (
                "(" + traverse(node.left) + ")" + str(node.val) + "(" + traverse(node.right) + ")"
            )
            counter[represantation] += 1
            if counter[represantation] == 2:
                output.append(node)
            return represantation
        counter = defaultdict(int)
        output = []
        traverse(root)
        return output

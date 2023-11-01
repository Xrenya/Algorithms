# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mapping = defaultdict(int)
        output = []
        def dfs(node):
            if not node:
                return
            mapping[node.val] += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        max_freq = max(mapping.values())
        for k, v in mapping.items():
            if v == max_freq:
                output.append(k)
        return output

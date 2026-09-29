# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        def dfs(node, path):
            if node is None:
                return None
            if not path:
                path += f"{node.val}"
            else:
                path += f"->{node.val}"
            left = dfs(node.left, path)
            right = dfs(node.right, path)
            if left is None and right is None:
                output.append(path[:])
            return node.val

        output = []
        dfs(root, "")
        return output

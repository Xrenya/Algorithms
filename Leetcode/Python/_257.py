class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        output = []
        def dfs(root,string):
            if not root: return
            if not (root.left or root.right):
                output.append(string + str(root.val))
            if root.left:
                dfs(root.left, string + str(root.val)+"->")
            if root.right:
                dfs(root.right, string + str(root.val)+"->")
        dfs(root, "")
        return output

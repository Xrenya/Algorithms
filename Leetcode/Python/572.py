# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        if not q and not p:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return not subRoot
        if not subRoot:
            return True
        ret = False
        if root.val == subRoot.val:
            ret = self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        if not ret:
            ret = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return ret
        

        

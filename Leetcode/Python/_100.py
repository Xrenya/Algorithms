# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not q and not p:
                return True
            elif (q and p) and (q.val == p.val):
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            return False
        
        return dfs(p, q)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([p, q])
        
        while queue:
            p = queue.popleft()
            q = queue.popleft()
            
            if not p and not q:
                continue
            
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            queue.append(p.left)
            queue.append(q.left)
            queue.append(p.right)
            queue.append(q.right)
            
        return True


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False
        if p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) 
        else:
            return False

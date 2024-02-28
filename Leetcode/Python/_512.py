class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max = -1
        self.bottom_val = 0
        
        def dfs(node, depth):
            if not node:
                return
            
            if depth > self.max:
                self.max = depth
                self.bottom_val = node.val
                
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            return        
        
        dfs(root, 0)
        return self.bottom_val

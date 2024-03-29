# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_map = {}
        output = []

        def findmax(root, level):
            if level not in level_map:
                level_map[level] = [root.val]
            else:
                level_map[level].append(root.val)

            level += 1
            if root.left:
                findmax(root.left, level)
            if root.right:
                findmax(root.right, level)
            if root.left == None and root.right == None:
                return root


        findmax(root,1)   

        for key, values in level_map.items():
            output.append(sum(values) / len(values))
        return output
    
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        result = []
        
        while q:
            n = len(q)
            level_sum = 0
            
            for _ in range(n):
                node = q.popleft()
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_sum / n)
        
        
        return result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = {}
        
        def dfs(node, x, y):
            if node:
                if y not in hashmap:
                    hashmap[y] = {}
                if x not in hashmap[y]:
                    hashmap[y][x] = []
                hashmap[y][x].append(node.val)
                dfs(node.left, x + 1, y - 1)
                dfs(node.right, x + 1, y + 1)                
            return
        
        def sort_temp(array):
            array = sorted(array, key=lambda x: x[0], reverse=False)
            array = [v for k, v in array]
            return array
        
        dfs(root, 0, 0)
        output = []
        for key_y, inside_dict in sorted(hashmap.items(), key=lambda x: x[0]):
            temp = []
            for key_x, values in sorted(inside_dict.items(), key=lambda x: x[0]):
                temp.extend(sorted(values))
            output.append(temp)
        return output

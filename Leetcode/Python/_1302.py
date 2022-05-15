# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deep_sum = depth = 0
        stack = [(root, depth)]
        
        while stack:
            node, cur_depth = stack.pop()
            if node.left is None and node.right is None:
                if depth < cur_depth:
                    deep_sum = node.val
                    depth = cur_depth
                    
                elif depth == cur_depth:
                    deep_sum += node.val
                    
            else:
                if node.left:
                    stack.append((node.left, cur_depth + 1))
                if node.right:
                    stack.append((node.right, cur_depth + 1))
        return deep_sum

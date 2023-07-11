# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Add additional information to parse back into tree 
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_parent(node, parent):
            if node:
                node.parent = parent
                add_parent(node.left, node)
                add_parent(node.right, node)

        add_parent(root, None)

        visited = set()
        output = []
        def dfs(node, k):
            if node and node not in visited:
                visited.add(node)
                if k == 0:
                    output.append(node.val)
                    return
                dfs(node.parent, k - 1)
                dfs(node.left, k - 1)
                dfs(node.right, k - 1)


        dfs(target, k)
        return output


class Solution:
    # Construct the graph to parse as usual
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def make_graph(node, parent):
            if node:
                if node and parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                if node.left:
                    make_graph(node.left, node)
                if node.right:
                    make_graph(node.right, node)

        make_graph(root, None)

        visited = set()
        output = []
        def dfs(node, k):
            if node not in visited:
                visited.add(node)
                if k == 0:
                    output.append(node)
                    return
                for next_node in graph[node]:
                    dfs(next_node, k - 1)

        dfs(target.val, k)
        return output

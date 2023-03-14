class Solution:
    def sumNumbers_v0(self, root: TreeNode):
        # time efficient solution
        root_to_leaf = 0
        stack = [(root, 0)]
        while stack:
            node, cur_sum = stack.pop()
            if node is not None:
                cur_sum = cur_sum * 10 + node.val
                if node.left is None and node.right is None:
                    root_to_leaf += cur_sum
                else:
                    stack.append((node.left, cur_sum))
                    stack.append((node.right, cur_sum))

        return root_to_leaf

    def sumNumbers_v1(self, root: TreeNode):
        # easy to write dfs solution
        self.total = 0
        self.dfs(root, 0)
        return self.total

    def dfs(self, node, cur_sum):
        if node:
            cur_sum = cur_sum * 10 + node.val
            if not node.left and not node.right:
                self.total += cur_sum
            self.dfs(node.left, cur_sum)
            self.dfs(node.right, cur_sum)

    def sumNumbers_v2(self, root: TreeNode):
        # constant space O(1)
        root_to_leaf = curr_number = 0

        while root:
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:
                # Predecessor node is one step to the left 
                # and then to the right till you can.
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = curr_number * 10 + root.val
                    predecessor.right = root
                    root = root.left
                    # Break the link predecessor.right = root
                # Once the link is broken, 
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number //= 10
                    predecessor.right = None
                    root = root.right

                    # If there is no left child
            # then just go right.        
            else:
                curr_number = curr_number * 10 + root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right

        return root_to_leaf

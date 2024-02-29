class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root])
        even = True
        while q:
            nodes = len(q)
            prev = maxsize
            if even:
                prev = -maxsize
                
            for _ in range(nodes):
                node = q.popleft()
                if (even and (node.val % 2 == 0 or node.val <= prev)) or \
                    (not even and (node.val % 2 == 1 or node.val >= prev)):
                    return False
                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            even = not even
        return True

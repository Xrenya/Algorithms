class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        depth = 0
        for string in s:
            if string is "(":
                depth += 1
            elif string is ")":
                depth -= 1
            if maxDepth < depth:
                maxDepth = depth
        return maxDepth

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        output = []
        depth = 0
        for c in seq:
            if c == "(":
                output.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                output.append(depth % 2)
        return output

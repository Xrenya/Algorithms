class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        output = 0
        for i in range(1, len(points)):
            output = max(output, points[i][0] - points[i - 1][0])
        return output

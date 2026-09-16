class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = -1
        output = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > stack:
                output.append(i)
                stack = heights[i]
        return output[::-1]

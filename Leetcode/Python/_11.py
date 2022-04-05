class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ans = 0
        while l < r:
            if heights[l] > heights[r]:
                vol = (r - l) * heights[r]
                r -= 1
            else:
                vol = (r - l) * heights[l]
                l += 1
            if vol > ans:
                ans = vol
        return ans
                
                
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maximum = 0
        while l < r:
            maximum = max(maximum, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maximum

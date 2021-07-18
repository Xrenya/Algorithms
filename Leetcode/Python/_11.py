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
                
                

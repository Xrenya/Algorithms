class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calc(heights, start, end):
            if start > end:
                return 0
            min_index = start
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(
                heights[min_index] * (end - start + 1),
                calc(heights, start, min_index - 1),
                calc(heights, min_index + 1, end)
            )
            
                
        return calc(heights, 0, len(heights) - 1)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = [0] * n
        for i in range(n):
            if not stack:
                stack.append(i)
                left[i] = i
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    left[i] = stack[-1] + 1
                else:
                    left[i] = 0
                stack.append(i)
        stack = []
        right = [0] * n
        for i in range(n - 1, -1, -1):
            if not stack:
                stack.append(i)
                right[i] = i
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    right[i] = stack[-1] - 1
                else:
                    right[i] = n - 1                 
                stack.append(i)
        area = 0
        for i in range(n):
            area = max(area, (right[i] - left[i] + 1) * heights[i])
        return area
                

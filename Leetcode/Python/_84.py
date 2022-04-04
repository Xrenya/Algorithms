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
                

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def calc_area(row):
            n = len(row)
            left = [0] * n
            right = [0] * n
            stack = []
            for i in range(n):
                if not stack:
                    stack.append(i)
                    left[i] = i
                else:
                    while stack and row[stack[-1]] >= row[i]:
                        stack.pop()
                    if stack:
                        left[i] = stack[-1] + 1
                    else:
                        left[i] = 0
                    stack.append(i)
            stack = []
            for i in range(n - 1, -1, -1):
                if not stack:
                    stack.append(i)
                    right[i] = i
                else:
                    while stack and row[stack[-1]] >= row[i]:
                        stack.pop()
                    if stack:
                        right[i] = stack[-1] - 1
                    else:
                        right[i] = n - 1
                    stack.append(i)
            area = 0
            for i in range(n):
                area = max(area, (right[i] - left[i] + 1) * row[i])
            return area
        output = [0] * len(matrix[0])
        area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num = int(matrix[i][j])
                if num != 0:
                    output[j] = output[j] + int(matrix[i][j])
                else:
                    output[j] = 0
            temp = calc_area(output)
            area = max(area, temp)
        return area
                

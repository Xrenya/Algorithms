class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
                else:
                    triangle[i][j] = min(triangle[i - 1][j - 1] + triangle[i][j], triangle[i - 1][j] + triangle[i][j])
        
        return min(triangle[-1])


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i + 1][j] + triangle[i][j], triangle[i + 1][j + 1] + triangle[i][j])
        
        return triangle[0][0]


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        dp = [[inf for _ in range(cols)] for cols in range(1, ROWS + 1)]
        dp[0] = triangle[0]

        for row in range(1, ROWS):
            for col in range(len(triangle[row])):
                right = dp[row - 1][col] if col < len(triangle[row - 1]) else inf
                left = dp[row - 1][col - 1] if col - 1 >= 0 else inf

                dp[row][col] = min(right + triangle[row][col], left + triangle[row][col])

        return min(dp[-1])


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        prev = triangle[0]
        
        for row in range(1, ROWS):
            cur = triangle[row]
            for col in range(len(triangle[row])):
                right = prev[col] if col < len(triangle[row - 1]) else inf
                left = prev[col - 1] if col - 1 >= 0 else inf

                cur[col] = min(right + triangle[row][col], left + triangle[row][col])
            prev = cur
        return min(prev)

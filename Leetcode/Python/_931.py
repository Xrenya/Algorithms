class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[float("inf")] * COLS for _ in range(ROWS)]
        dp[0] = matrix[0]
        for row in range(1, ROWS):
            for col in range(COLS):
                for d in [-1, 0, 1]:
                    n_row = row - 1
                    n_col = d + col
                    if 0 <= n_row < ROWS and 0 <= n_col < COLS:
                        dp[row][col] = min(dp[row][col], dp[n_row][n_col] + matrix[row][col])
        return min(dp[-1])

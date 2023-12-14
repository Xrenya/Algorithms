class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        col_ones = [0] * cols
        row_ones = [0] * rows
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    row_ones[row] += 1
                    col_ones[col] += 1
        dif = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                dif[row][col] = row_ones[row] + col_ones[col] - (rows - row_ones[row]) - (cols - col_ones[col])
        return dif

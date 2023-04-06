class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if (row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1) and (grid[row][col] == 0 or grid[row][col] == 3):
                grid[row][col] = 3
                return 0
            elif 0 < row < ROWS and 0 < col < COLS and grid[row][col] == 0:
                grid[row][col] = 2
                return dfs(row - 1, col) * dfs(row, col - 1) * dfs(row, col + 1) * dfs(row + 1, col)
            return 1
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    count += dfs(row, col)
        # for row in range(ROWS):
        #     print(*grid[row])
        return count

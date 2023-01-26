class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(row, col):
            if 0 <= row < ROWS and 0 <= col < COLS and grid1[row][col] == 1 and grid2[row][col] == 1:
                grid1[row][col] = 2
                grid2[row][col] = 2
                return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
            elif 0 <= row < ROWS and 0 <= col < COLS and grid1[row][col] == 0 and grid2[row][col] == 1:
                return -float("inf")
            return 0

        ROWS = len(grid1)
        COLS = len(grid1[0])
        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid1[row][col] == grid2[row][col] and grid1[row][col] == 1:
                    count += 1 if dfs(row, col) > 0 else 0
        return count

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        min_changes = [[float("inf")] * cols for _ in range(rows)]
        min_changes[0][0] = 0

        while True:
            prev = [row[:] for row in min_changes]

            for row in range(rows):
                for col in range(cols):
                    if row > 0:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row - 1][col]
                            + (0 if grid[row - 1][col] == 3 else 1)
                        )
                    if col > 0:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row][col - 1]
                            + (0 if grid[row][col - 1] == 1 else 1)
                        )
            for row in range(rows - 1, -1, -1):
                for col in range(cols - 1, -1, -1):
                    if row < rows - 1:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row + 1][col]
                            + (0 if grid[row + 1][col] == 4 else 1)
                        )
                    if col < cols - 1:
                        min_changes[row][col] = min(
                            min_changes[row][col],
                            min_changes[row][col + 1]
                            + (0 if grid[row][col + 1] == 2 else 1)
                        )
            if min_changes == prev:
                break

        return min_changes[rows - 1][cols - 1]
            

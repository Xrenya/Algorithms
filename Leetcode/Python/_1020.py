class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        queue = deque([])
        ROWS = len(grid)
        COLS = len(grid[0])
        total = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    total += 1
                    if row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1:
                        queue.append((row, col))
                        grid[row][col] = 0

        while queue:
            r, c = queue.popleft()
            total -= 1
            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                row = r + dx
                col = c + dy
                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                    grid[row][col] = 0
                    queue.append((row, col))

        return total
      
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if 0 < row < ROWS - 1 and 0 < col < COLS - 1 and grid[row][col] == 1:
                grid[row][col] = 3
                return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
            if 0 <= row <= ROWS - 1 and 0 <= col <= COLS - 1 and grid[row][col] == 0:
                return 0
            elif row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1 or grid[row][col] == 1:
                grid[row][col] = 2
                return -float("inf")
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        cnt = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    out = dfs(row, col)
                    cnt += max(0, out)
        return cnt

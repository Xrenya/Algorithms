class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ROWS = len(grid)
        COLS = len(grid[0])
        dist = 0
        queue = deque([])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    queue.append((row, col))
        while queue:
            row, col = queue.popleft()
            for r, c in dirs:
                new_row, new_col = row + r, col + c
                if new_row < 0 or new_row == ROWS or new_col < 0 or new_col == COLS or grid[new_row][new_col]:
                    continue
                queue.append((new_row, new_col))
                grid[new_row][new_col] = grid[row][col] + 1
                dist = max(dist, grid[new_row][new_col])
        return dist - 1

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque([])
        ROWS = len(grid)
        COLS = len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    queue.append((row, col))

        while queue:
            r, c = queue.popleft()
            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                row = r + dx
                col = c + dy
                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 0:
                    grid[row][col] = grid[r][c] + 1
                    queue.append((row, col))
                elif  0 <= row < ROWS and 0 <= col < COLS and grid[row][col] > grid[r][c] + 1:
                    grid[row][col] = grid[r][c] + 1
                    queue.append((row, col))

        dist = -1
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] > 1:
                    dist = max(dist, grid[row][col])
        return dist - 1 if dist != -1 else -1

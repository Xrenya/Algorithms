class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        good = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque([])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    good += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
        if good == 0:
            return 0
        DIRS = ((-1, 0), (0, -1), (1, 0), (0, 1))
        cnt = 0
        while queue:
            n = len(queue)
            flag = False
            for _ in range(n):
                r, c = queue.popleft()
                for dx, dy in DIRS:
                    row = r + dx
                    col = c + dy
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] not in (0, 2):
                        grid[row][col] = 2
                        good -= 1
                        flag += 1
                        queue.append((row, col))
            if flag:
                cnt += 1
        return cnt if good == 0 else -1

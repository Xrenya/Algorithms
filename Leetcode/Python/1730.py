class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        q = deque([])
        ROWS = len(grid)
        COLS = len(grid[0])
        foods = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 'X' or grid[i][j] == '0':
                    continue
                elif grid[i][j] == '*':
                    q.append((i, j, 0))
                elif grid[i][j] == '#':
                    foods.add((i, j))

        if len(foods) == 0 or len(q) == 0:
            return -1

        grid[q[0][0]][q[0][1]] = 'X'
        
        while q:
            x, y, steps = q.popleft()
            if (x, y) in foods:
                return steps
            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                nx = dx + x
                ny = dy + y
                if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] != 'X':
                    q.append((nx, ny, steps + 1))
                    grid[nx][ny] = 'X'
        return -1

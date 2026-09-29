class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ')':
            return False
        if (m + n - 1) % 2 != 0:
            return False
        @cache
        def dfs(x, y, opened):
            if x == m - 1 and y == n - 1:
                return opened == 0
            if x < 0 or x >= m or y < 0 or y >= n and (x + y):
                return False
            if opened > m - x + n - y - 2:
                return False
            for dx, dy in [(1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if nx < m and ny < n:
                    if grid[nx][ny] == '(':
                        if dfs(nx, ny, opened + 1):
                            return True
                    else:
                        if opened > 0 and dfs(nx, ny, opened - 1):
                            return True
            return False
        return dfs(0, 0, 1)

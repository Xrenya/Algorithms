class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def pprint(grid):
            for row in grid:
                print(row)
            print()

        def dfs(row, col):
            if 0 <= row < ROWS and 0 <= col < COLS and (row, col) not in visited and grid[row][col]:
                grid[row][col] = 2
                queue.append((row, col, 2))
                visited.add((row, col))
                for r, c in dirs:
                    dfs(row + r, col + c)

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque()
        flag = False
        for row in range(ROWS):
            for col in range(COLS):
                print(grid[row][col])
                if grid[row][col]:
                    dfs(row, col)
                    flag = True
                    break
            if flag:
                break

        minimum = float("inf")
        while queue:
            row, col, cur_dist = queue.popleft()
            for r, c in dirs:
                new_row, new_col, new_dist = row + r, col + c, cur_dist + 1
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    if not grid[new_row][new_col]:
                        grid[new_row][new_col] = new_dist
                        queue.append((new_row, new_col, new_dist))
                    else:
                        minimum = min(minimum, new_dist)
        return minimum - 3

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            visited = set()
            queue = deque([(x, y, 1)])
            while queue:
                row, col, dist = queue.popleft()
                visited.add((row, col))
                for r, c in DIRS:
                    new_row = row + r
                    new_col = col + c
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col, dist + 1))
                        grid[new_row][new_col] = dist + 1
            return

        if grid[-1][-1] != 0 or grid[0][0] == 1:
            return -1
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = ((-1, 0), (-1, -1), (0, -1), (1, -1), (0, 1), (1, 1), (1, 0), (-1, 1))
        grid[0][0] = 1
        bfs(0, 0)
        print(grid)
        return grid[-1][-1] if grid[-1][-1] > 0 else -1


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bfs(queue):
            visited = set()
            while queue:
                r, c, d = queue.popleft()
                visited.add((r, c))
                for x, y in DIRS:
                    row = x + r
                    col = y + c
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 0 and (row, col) not in visited:
                        queue.append((row, col, d + 1))
                        grid[row][col] = d + 1
            return
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = ((-1, 0), (-1, -1), (0, -1), (1, -1), (0, 1), (1, 1), (1, 0), (-1, 1))
        if grid[0][0] != 0 or len(grid[0]) == 0 or grid[-1][-1] != 0:
            return -1
        grid[0][0] = 1
        bfs(deque([(0, 0, 1)]))
        return grid[-1][-1] if grid[-1][-1] else -1
    
    
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        
        DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        def get_neighbours(row, col):
            for row_difference, col_difference in DIRECTIONS:
                new_row, new_col = row + row_difference, col + col_difference
                if  not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield new_row, new_col
        
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1
        
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance
        
            for cur_row, cur_col in get_neighbours(row, col):
                grid[cur_row][cur_col] = distance + 1
                queue.append((cur_row, cur_col))
                
        return -1

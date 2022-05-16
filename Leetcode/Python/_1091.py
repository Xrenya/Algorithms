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

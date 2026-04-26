class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        parent = list(range(ROWS * COLS))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return True  # Cycle detected
            parent[root_y] = root_x
            return False
        
        for i in range(ROWS):
            for j in range(COLS):
                idx = i * COLS + j
                # Check right neighbor
                if j + 1 < COLS and grid[i][j] == grid[i][j + 1]:
                    if union(idx, idx + 1):
                        return True
                # Check bottom neighbor
                if i + 1 < ROWS and grid[i][j] == grid[i + 1][j]:
                    if union(idx, idx + COLS):
                        return True
        
        return False
      
    def containsCycleDfs(self, grid: List[List[str]]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        
        def dfs(row, col, parent_row, parent_col, char, length):
            if visited[row][col]:
                return length >= 4
            
            visited[row][col] = True
            
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == char:
                    if nr == parent_row and nc == parent_col:
                        continue
                    
                    if dfs(nr, nc, row, col, char, length + 1):
                        return True
            
            return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j], 1):
                        return True
        
        return False

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        DIRS = ((1,0),(-1,0),(0,1),(0,-1))
        if start == destination:
            return 0

        queue = deque([[start[0], start[1], 0]])
        visited =  { tuple(start) : 0 }
        output = []
        while queue:
            row, col, dist = queue.popleft()
            for xr, xc in DIRS:
                new_row = row
                new_col = col
                new_dist = dist
                while 0 <= new_row + xr < ROWS and 0 <= new_col + xc < COLS and maze[new_row + xr][new_col + xc] == 0:
                    new_row += xr
                    new_col += xc
                    new_dist += 1
                if [new_row, new_col] == destination:
                    output.append(new_dist)
                    continue
                
                if ((new_row, new_col) in visited and visited[(new_row, new_col)] > new_dist) or (new_row, new_col) not in visited:
                    visited[(new_row, new_col)] = new_dist
                    queue.append((new_row, new_col, new_dist))
        return min(output) if output else -1

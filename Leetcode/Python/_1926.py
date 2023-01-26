class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def pprint(grid):
            for row in grid:
                print(row)
            print()

        #pprint(maze)
        ROWS, COLS = len(maze), len(maze[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col = entrance
        maze[row][col] = "+"
        queue = deque()
        queue.append((row, col, 0))

        while queue:
            row, col, dist = queue.popleft()
            for r, c in DIRS:
                new_row, new_col, new_dist = row + r, col + c, dist + 1
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and maze[new_row][new_col] == ".":
                    if new_row == 0 or new_col == 0 or new_col == COLS - 1 or new_row == ROWS - 1:
                        return new_dist
                    maze[new_row][new_col] = "+"
                    queue.append((new_row, new_col, new_dist))

        return -1

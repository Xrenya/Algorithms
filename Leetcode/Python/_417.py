class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue):
            visited = set()
            while queue:
                cur_row, cur_col = queue.popleft()
                visited.add((cur_row, cur_col))
                for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    row = cur_row + x
                    col = cur_col + y
                    if 0 <= row < ROWS and 0 <= col < COLS and heights[cur_row][cur_col] <= heights[row][col] and (row, col) not in visited:
                        queue.append((row, col))
            return visited


        pacific = deque([])
        atlantic = deque([])
        ROWS = len(heights)
        COLS = len(heights[0])
        for row in range(ROWS):
            pacific.append((row, 0))
            atlantic.append((row, COLS - 1))
        for col in range(COLS):
            pacific.append((0, col))
            atlantic.append((ROWS - 1, col))

        visited_pacific = bfs(pacific)
        visited_atlantic = bfs(atlantic)
        return list(visited_pacific.intersection(visited_atlantic))


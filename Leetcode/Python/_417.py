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


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not matrix or not matrix[0]: 
            return []
            
        num_rows, num_cols = len(matrix), len(matrix[0])

        # Setup each queue with cells adjacent to their respective ocean
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(num_rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, num_cols - 1))
        for i in range(num_cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((num_rows - 1, i))
        
        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                # This cell is reachable, so mark it
                reachable.add((row, col))
                for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
                    new_row, new_col = row + x, col + y
                    # Check if the new cell is within bounds
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    # Check that the new cell hasn't already been visited
                    if (new_row, new_col) in reachable:
                        continue
                    # Check that the new cell has a higher or equal height,
                    # So that water can flow from the new cell to the old cell
                    if matrix[new_row][new_col] < matrix[row][col]:
                        continue
                    # If we've gotten this far, that means the new cell is reachable
                    queue.append((new_row, new_col))
            return reachable
        
        # Perform a BFS for each ocean to find all cells accessible by each ocean
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS = len(mat)
        COLS = len(mat[0])
        if ROWS == 0:
            return mat
        dst = [[float("inf")] * COLS for _ in range(ROWS)]
        queue = deque([])
        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0:
                    dst[row][col] = 0
                    queue.append((row, col))
        DIRS = ((-1, 0), (0, -1), (1, 0), (0, 1))
        while queue:
            row, col = queue.popleft()
            for dx, dy in DIRS:
                new_row = row + dx
                new_col = col + dy
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and dst[new_row][new_col] > dst[row][col] + 1:
                    dst[new_row][new_col] = dst[row][col] + 1
                    queue.append((new_row, new_col))
        return dst

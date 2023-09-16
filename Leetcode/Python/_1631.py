class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        diff = [[float("inf")] * COLS for _ in range(ROWS)]
        diff[0][0] = 0
        visited = [[False] * COLS for _ in range(ROWS)]
        queue = [(0, 0, 0)] # diff, x, y
        while queue:
            dif, x, y = heapq.heappop(queue)
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adj_x = x + dx
                adj_y = y + dy
                if 0 <= adj_x < ROWS and 0 <= adj_y < COLS and not visited[adj_x][adj_y]:
                    cur_dif = abs(heights[adj_x][adj_y] - heights[x][y])
                    max_dif = max(cur_dif, diff[x][y])
                    if diff[adj_x][adj_y] > max_dif:
                        diff[adj_x][adj_y] = max_dif
                        heapq.heappush(queue, (max_dif, adj_x, adj_y))
        return diff[-1][-1]

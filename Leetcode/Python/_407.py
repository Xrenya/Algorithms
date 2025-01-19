class Cell:
    def __init__(self, height, row, col):
        self.height = height
        self.row = row
        self.col = col

    def __lt__(self, other):
        return self.height < other.height


class Solution:
    def is_valid_cell(self, row, col, rows, cols):
        return 0 <= row < rows and 0 <= col < cols

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        drow = [0, 0, -1, 1]
        dcol = [-1, 1, 0, 0]

        rows = len(heightMap)
        cols = len(heightMap[0])

        visited = [[False] * cols for _ in range(rows)]

        boundary = []

        for i in range(rows):
            heapq.heappush(boundary, Cell(heightMap[i][0], i, 0))
            heapq.heappush(
                boundary,
                Cell(heightMap[i][cols - 1], i, cols - 1)
            )
            visited[i][0] = visited[i][cols - 1] = True

        for i in range(cols):
            heapq.heappush(boundary, Cell(heightMap[0][i], 0, i))
            heapq.heappush(
                boundary,
                Cell(heightMap[rows - 1][i], rows - 1, i)
            )
            visited[0][i] = visited[rows - 1][i] = True

        volume = 0

        while boundary:
            cell = heapq.heappop(boundary)

            cur_row = cell.row
            cur_col = cell.col
            min_boundary = cell.height

            for d in range(4):
                nrow = cur_row + drow[d]
                ncol = cur_col + dcol[d]

                if (
                    self.is_valid_cell(nrow, ncol, rows, cols)
                    and not visited[nrow][ncol]
                ):
                    nheight = heightMap[nrow][ncol]

                    if nheight < min_boundary:
                        volume += (min_boundary - nheight)
                    
                    heapq.heappush(
                        boundary,
                        Cell(
                            max(nheight, min_boundary),
                            nrow,
                            ncol
                        )
                    )
                    visited[nrow][ncol] = True

        return volume


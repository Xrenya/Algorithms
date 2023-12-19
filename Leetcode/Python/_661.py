class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        output = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                acc = img[row][col]
                count = 1
                for delta in [-1, 1]:
                    new_row = row + delta
                    if 0 <= new_row < rows:
                        count += 1
                        acc += img[new_row][col]

                for delta in [-1, 1]:
                    new_col = col + delta
                    if 0 <= new_col < cols:
                        count += 1
                        acc += img[row][new_col]
                        

                for row_delta, col_delta in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
                    new_row = row + row_delta
                    new_col = col + col_delta
                    if 0 <= new_col < cols and 0 <= new_row < rows:
                        count += 1
                        acc += img[new_row][new_col]

                output[row][col] = acc // count

        return output

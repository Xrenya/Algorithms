class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    rows.append(i)
                    cols.append(j)
        for i, row in enumerate(matrix):
            if i in rows:
                matrix[i] = [0] * len(matrix[i])
            for j, col in enumerate(row):
                if j in cols:
                    matrix[i][j] = 0

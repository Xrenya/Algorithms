class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zeros = False
        col_zeros = False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            if matrix[i][0] == 0:
                col_zeros = True
                
        for j in range(cols):
            if matrix[0][j] == 0:
                row_zeros = True   
                    
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if row_zeros:
            for j in range(cols):
                matrix[0][j] = 0
                
        if col_zeros:
            for i in range(rows):
                matrix[i][0] = 0
        
        
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
                continue
            for j, col in enumerate(row):
                if j in cols:
                    matrix[i][j] = 0

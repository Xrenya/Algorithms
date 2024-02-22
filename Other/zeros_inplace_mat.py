# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag, col_flag = False, False
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in range(ROWS):
            if matrix[row][0] == 0:
                col_flag = True
                break
        
        for col in range(COLS):
            if matrix[0][col] == 0:
                row_flag = True
                break

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[0][col] == 0:
                    matrix[row][col] = 0
                if matrix[row][0] == 0:
                    matrix[row][col] = 0

        if col_flag:
            for row in range(ROWS):
                matrix[row][0] = 0

        if row_flag:
            for col in range(COLS):
                matrix[0][col] = 0



        

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        acc = 0
        for row in range(rows):
            if row != rows - row - 1:
                acc += mat[row][row] + mat[row][rows - row - 1]
            else:
                acc += mat[row][row]
        return acc
    
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # Time complexity O(n)
        acc = 0
        n = len(mat)
        for idx in range(n):
            acc += mat[idx][idx] + mat[idx][n - 1 - idx]
        if len(mat) % 2 == 1:
            acc -= mat[n // 2][n // 2]
        return acc

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        left, top, right, bottom = 0, 0, n, n
        val = 1
        while left < right and top < bottom:
            for i in range(left, right):
                mat[top][i] = val
                val += 1
            top += 1
            
            for i in range(top, bottom):
                mat[i][right - 1] = val
                val += 1
            right -= 1
            
            for i in range(right - 1, left - 1, -1):
                mat[bottom - 1][i] = val
                val += 1
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1):
                mat[i][left] = val
                val += 1
            left += 1
        return mat

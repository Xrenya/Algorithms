class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:       
        l = -1
        row = len(matrix)
        col = len(matrix[0])
        r = row * col
        while l < r - 1:
            m = l + (r - l) // 2
            rw, cw = divmod(m, col)
            # print(l, m, r, rw, cw)
            if matrix[rw][cw] == target:
                return True
            elif matrix[rw][cw] < target:
                l = m
            else:
                r = m
        return False

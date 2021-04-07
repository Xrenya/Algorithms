class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # Time complexity O(n)
        acc = 0
        for idx in range(len(mat)):
            acc += mat[idx][idx] + mat[idx][len(mat)-1-idx]
        if len(mat) %2 == 1:
            acc -= mat[len(mat)//2][len(mat)//2]
        return acc

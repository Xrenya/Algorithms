class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        row_c = [0] * rows
        col_c = [0] * cols
        
        for row in range(rows):
            for col in range(cols):
                if mat[row][col]:
                    row_c[row] += 1
                    col_c[col] += 1
                    
        output = 0
        for row in range(rows):
            for col in range(cols):
                if mat[row][col]:
                    if row_c[row] == 1 and col_c[col] == 1:
                        output += 1
        return output


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        for col in zip(*mat):
            res, idx = self.summator(col)
            if res == 1:
                res1 ,idx1 = self.summator(mat[idx])
                if res1 == 1:
                    count += 1
        return count
    
    def summator(self, mat):
        acc = 0
        idx = 0
        for i, num in enumerate(mat):
            num = num
            acc += num 
            if num == 1:
                idx = i
        return acc, idx
                

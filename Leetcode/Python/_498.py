class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        diag = len(mat) + len(mat[0]) - 1
        max_row = len(mat)
        max_col = len(mat[0])
        row = col = 0
        output = []
        for d in range(diag):
            temp = []
            
            row = 0 if d < max_col else d - max_col + 1
            col = d if d < max_col else max_col - 1
            
            while row < max_row and col > -1:
                temp.append(mat[row][col])
                row += 1
                col -= 1
                
            if d % 2 == 0:
                output.extend(temp[::-1])
            else:
                output.extend(temp)
                
        return output

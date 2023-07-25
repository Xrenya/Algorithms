class Solution:
    def __init__(self):
        self.memo = {}
        
    def getCol(self, row, col):
        if row == 0 or col == 0 or row == col:
            return 1

        if (row, col) in self.memo:
            return self.memo[(row, col)]

        self.memo[(row, col)] = self.getCol(row - 1, col - 1) + self.getCol(row - 1, col)
        
        return self.memo[(row, col)]

    def getRow(self, rowIndex: int) -> List[int]:
        output = []
        
        for row in range(rowIndex + 1):
            output.append(self.getCol(rowIndex, row))
        return output


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [1, 1]
        if rowIndex == 0:
            return [1]
        for i in range(2, rowIndex + 1):
            temp = [1] * (i + 1)
            for i in range(1, i):
                temp[i] = output[i - 1] + output[i]
            output = temp[:]
        return output

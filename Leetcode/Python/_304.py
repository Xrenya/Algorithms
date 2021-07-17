class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_maxtrix = self.prefix()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        acc = 0
        for row in range(row1, row2+1):
            acc += self.prefix_maxtrix[row][col2 + 1] - self.prefix_maxtrix[row][col1]
        return acc
        
    def prefix(self):
        prefix_maxtrix = []
        for row in self.matrix:
            prefixsum = [0] * (len(row) + 1) 
            for i in range(1, len(row) + 1):
                prefixsum[i] = prefixsum[i-1] + row[i-1]
            prefix_maxtrix.append(prefixsum)
        return prefix_maxtrix

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

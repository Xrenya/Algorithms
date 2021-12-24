class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        output = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            output.append([1] * i)
            for i in range(1, i - 1):
                output[-1][i] = output[-2][i - 1] + output[-2][i]
        return output

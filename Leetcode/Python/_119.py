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

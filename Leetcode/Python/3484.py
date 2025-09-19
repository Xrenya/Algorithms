class Spreadsheet:

    def __init__(self, rows: int):
        self.array = [[0 for _ in range(ord("Z") - ord("A") + 1)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        self.array[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord("A")
        row = int(cell[1:]) - 1
        self.array[row][col] = 0        

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        left, right = formula.split("+")
        if left[0].isalpha():
            col = ord(left[0]) - ord("A")
            row = int(left[1:]) - 1
            left = self.array[row][col]
        else:
            left = int(left)
        if right[0].isalpha():
            col = ord(right[0]) - ord("A")
            row = int(right[1:]) - 1
            right = self.array[row][col]
        else:
            right = int(right)
        return left + right
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

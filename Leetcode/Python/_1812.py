class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        hashMap = {"a":1, "b":2, "c":3, "d":4,
                   "e":5, "f":6, "g":7, "h":8}
        row, col = int(coordinates[1]), hashMap[coordinates[0]]
        if (row%2 != 0 and col%2 != 0) or (row%2 == 0 and col%2 == 0):
            return False
        else:
            return True

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        hashMap = {"a":1, "b":2, "c":3, "d":4,
                   "e":5, "f":6, "g":7, "h":8}
        row, col = int(coordinates[1]), hashMap[coordinates[0]]
        if row%2==col%2:
            return False
        else:
            return True

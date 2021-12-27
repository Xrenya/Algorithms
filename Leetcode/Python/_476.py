class Solution:
    def findComplement(self, num: int) -> int:
        lenght = len(bin(num)) - 2
        ONE = 1
        for x in range(lenght - 1):
            ONE = ONE << 1
            ONE = ONE | 1
        return num^ONE

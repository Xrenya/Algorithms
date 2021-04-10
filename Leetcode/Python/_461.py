class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binary_x = bin(x)[2:]
        binary_y = bin(y)[2:]
        if len(binary_x) > len(binary_y):
            binary_y = '0'*(len(binary_x)-len(binary_y)) + binary_y
        elif len(binary_x) < len(binary_y):
            binary_x = '0'*(len(binary_y)-len(binary_x)) + binary_x
        count = 0
        for idx in range(len(binary_x)):
            if binary_y[idx] != binary_x[idx]:
                count += 1
        return count
      
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binary = bin(x^y)
        count = 0
        for s in binary:
            if s == "1":
                count += 1
        return count

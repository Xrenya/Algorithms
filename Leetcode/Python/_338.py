class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(n + 1):
            output[i] =  output[i >> 1] + i % 2
        return output

class Solution:
    def countBits(self, n: int) -> List[int]:
        array = []
        for i in range(n + 1):
            array.append(bin(i).count("1"))
        return array

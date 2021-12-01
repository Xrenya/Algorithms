class Solution:
    def countBits(self, n: int) -> List[int]:
        array = []
        for i in range(n + 1):
            array.append(bin(i).count("1"))
        return array

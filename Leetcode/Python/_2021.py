class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        array = []
        for i in range(0, len(original) // n):
            array.append(original[i * n:(i + 1) * n])
        return array

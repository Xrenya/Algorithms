class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = []
        for col in zip(*matrix):
            output.append(col)
        return output

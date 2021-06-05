class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [*map(list, zip(*A))]
    
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = []
        for col in zip(*matrix):
            output.append(col)
        return output

class Solution:
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        mins = set([min(m) for m in mat])
        maxes = set([max(i) for i in zip(*mat)])
        return mins.intersection(maxes)
      
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        def minimum(array):
            min_num = +inf
            for num in array:
                if num < min_num:
                    min_num = num
            return min_num
        
        def maximum(array):
            max_num = -inf
            for num in array:
                if num > max_num:
                    max_num = num
            return max_num
        
        def make_col_array(array, rows, col):
            new_array = []
            for row in range(rows):
                new_array.append(array[row][col])
            return new_array

        maxs = []
        mins = []
        for mat in matrix:
            mins.append(minimum(mat))
        for mat in zip(*matrix):
            maxs.append(maximum(list(mat)))
        return set(mins).intersection(set(maxs))
            
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        def minimum(array):
            idx = 0
            i = 0
            min_num = +inf
            for num in array:
                if num < min_num:
                    min_num = num
                    idx = i
                i += 1
            return idx
        
        def maximum(array):
            idx = 0
            i = 0
            max_num = -inf
            for num in array:
                if num > max_num:
                    max_num = num
                    idx = i
                i += 1
            return idx
        
        def make_col_array(array, rows, col):
            new_array = []
            for row in range(rows):
                new_array.append(array[row][col])
            return new_array
        
        lucky = []
        
        for row in range(len(matrix)):
            idx = minimum(matrix[row])
            array = make_col_array(matrix, len(matrix), idx)
            if matrix[row][idx] == array[maximum(array)]:
                lucky.append(matrix[row][idx])
        
        return lucky

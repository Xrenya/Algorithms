class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        for col in zip(*mat):
            res, idx = self.summator(col)
            if res == 1:
                res1 ,idx1 = self.summator(mat[idx])
                if res1 == 1:
                    count += 1
        return count
    
    def summator(self, mat):
        acc = 0
        idx = 0
        for i, num in enumerate(mat):
            num = num
            acc += num 
            if num == 1:
                idx = i
        return acc, idx
                

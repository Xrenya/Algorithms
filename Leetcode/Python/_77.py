class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(first, lst):
            if len(lst) == k:
                output.append(lst[:])
                return 
            for i in range(first, n + 1):
                lst.append(i)
                backtrack(i + 1,  lst)
                lst.pop()
            
            return
        backtrack(1, [])
        return output

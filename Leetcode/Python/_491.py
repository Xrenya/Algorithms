class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = set()
        seq = []
        def backtrack(index: int):
            if index == n:
                if len(seq) >= 2:
                    output.add(tuple(seq))
                return
            num = nums[index]
            if not seq or seq[-1] <= num:
                seq.append(num)
                backtrack(index + 1)
                seq.pop()
            backtrack(index + 1)
            return

        backtrack(0)
        return output

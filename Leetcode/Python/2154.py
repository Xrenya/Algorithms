class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mapping = {}
        for n in nums:
            mapping[n] = 1
        while original in mapping:
            original *= 2
        return original

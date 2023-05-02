class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for val  in nums:
            if val == 0:
                return 0
            product *= val
        return 1 if product > 0 else -1

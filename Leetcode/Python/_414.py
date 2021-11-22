class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_1 = -inf
        max_2 = -inf
        max_3 = -inf
        for num in nums:
            if max_1 < num:
                max_3 = max_2
                max_2 = max_1
                max_1 = num
            elif max_2 < num and num != max_1:
                max_3 = max_2
                max_2 = num
            elif max_3 < num and max_2 != num and max_1 != num:
                max_3 = num
        if max_3 == -inf:
            return max(max_1, max_2, max_3)
        return max_3
                

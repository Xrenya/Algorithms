class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = nums1[0]
        odd = 0
        for num in nums1:
            if num < n:
                n = num
            if num & 1:
                odd += 1

        if n & 1:
            return True
        return odd == 0

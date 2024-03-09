class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        min_val = float("inf")

        for val in set(nums1).intersection(set(nums2)):
            if val < min_val:
                min_val = val

        return -1 if min_val == float("inf") else min_val

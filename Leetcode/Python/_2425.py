class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1), len(nums2)

        freq = {}

        for n in nums1:
            freq[n] = freq.get(n, 0) + len2

        for n in nums2:
            freq[n] = freq.get(n, 0) + len1

        output = 0
        for n in freq:
            if freq[n] % 2:
                output ^= n
        return output

from collections import defaultdict


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashMap_1 = defaultdict(int)
        hashMap_2 = defaultdict(int)
        for num in nums1:
            hashMap_1[num] += 1
        for num in nums2:
            hashMap_2[num] += 1
        output = []
        for key, val in hashMap_1.items():
            value = hashMap_2.get(key, 0)
            output += [key] * min(value, val)
        return output

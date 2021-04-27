class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set.intersection(set(nums1), set(nums2))
      
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        array = []
        if len(nums1) > len(nums2):
            for num in nums2:
                if num in nums1 and num not in array:
                    array.append(num)
                else:
                    continue
        else:
            for num in nums1:
                if num in nums2 and num not in array:
                    array.append(num)
                else:
                    continue
        return array

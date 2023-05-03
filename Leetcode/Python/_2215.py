class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        return (nums1.difference(nums2), nums2.difference(nums1))
      
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        def mapping(num):
            num_mapping = {}
            for n in num:
                if n not in num_mapping:
                    num_mapping[n] = 0
                num_mapping[n] += 1
            return num_mapping

        mapping_nums1 = mapping(nums1)
        mapping_nums2 = mapping(nums2)
        output = [[], []]

        for key, value in mapping_nums1.items():
            if key not in mapping_nums2:
                output[0].append(key)
            else:
                del mapping_nums2[key]

        output[1].extend(mapping_nums2.keys())

        return output

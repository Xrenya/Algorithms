from typing import List

# Given two sorted array
# Find the intersection (common values in both arrays)


def findIntersectionValues(nums1: List[int], nums2: List[int]) -> List[int]:   
    p1 = p2 = 0
    len_1 = len(nums1)
    len_2 = len(nums2)

    output = []
    while p1 < len_1 and p2 < len_2:
            if nums1[p1] == nums2[p2]:
                output.append(nums2[p2])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                p1 += 1
                
    return output
    

nums1 = [-10, -5, 2, 5, 6, 8]
nums2 = [2, 5, 7, 8]

# Expected output: [2, 5, 8]
print(findIntersectionValues(nums1, nums2))

class Solution:
    def findMedianSortedArraysBrute(self, nums1: List[int], nums2: List[int]) -> float:
        """Merge two array, sort it and jsut find the median of a sorted array
        """
        merge = nums1 + nums2
        merge = sorted(merge)
        if len(merge) % 2 != 0:
            return merge[len(merge) // 2]
        else:
            return (merge[len(merge) // 2] + merge[len(merge) // 2 - 1])/2
   def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Using Binary Search
        """
       pass
                         

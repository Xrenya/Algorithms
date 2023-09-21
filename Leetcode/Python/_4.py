class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Complexity O(n + m)
        m = len(nums1) + len(nums2)
        if m % 2 == 1:
            left = right = m // 2
        else:
            left, right = m // 2 - 1, m // 2
        l1, l2 = 0, 0
        output = 0
        while l1 < len(nums1) and l2 < len(nums2):
            if l1 < len(nums1) and nums1[l1] < nums2[l2]:
                if (l1 + l2) == left:
                    output += nums1[l1]
                elif (l1 + l2) == right:
                    output += nums1[l1]
                l1 += 1
            else:
                if (l1 + l2) == left:
                    output += nums2[l2]
                elif (l1 + l2) == right:
                    output += nums2[l2]
                l2 += 1
        while l1 < len(nums1):
            if (l1 + l2) == left:
                output += nums1[l1]
            elif (l1 + l2) == right:
                output += nums1[l1]
            l1 += 1
        while l2 < len(nums2):
            if (l1 + l2) == left:
                output += nums2[l2]
            elif (l1 + l2) == right:
                output += nums2[l2]
            l2 += 1
        
        return output / 2 if left != right else output
        

class Solution:
    def findMedianSortedArraysBrute(self, nums1: List[int], nums2: List[int]) -> float:
        """Merge two array, sort it and jsut find the median of a sorted array
        Complexity O((m + n) log(m + n))
        """
        merge = nums1 + nums2
        merge = sorted(merge)
        if len(merge) % 2 != 0:
            return merge[len(merge) // 2]
        else:
            return (merge[len(merge) // 2] + merge[len(merge) // 2 - 1])/2

                         

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low = 0
        high = len(A) - 1
        while low <= high:
            mid = low + (high - low)//2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                return mid
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
                
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while True:
            mid = (l + r) // 2
            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid
            elif arr[mid]>arr[mid+1]:
                r = mid + 1
            else:
                l = mid

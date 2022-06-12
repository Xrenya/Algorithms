class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maximum = 0
        numset = set()
        left = 0
        temp = 0
        for right in range(len(nums)):
            if nums[right] in numset:
                while nums[right] != nums[left]:
                    numset.remove(nums[left])
                    temp -= nums[left]
                    left += 1
                left += 1
            else:
                numset.add(nums[right])
                temp += nums[right]
            maximum = max(maximum, temp)
        return maximum

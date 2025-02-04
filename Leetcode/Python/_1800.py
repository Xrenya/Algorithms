class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        acc = 0
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                acc = max(acc, cur)
                cur = 0
            cur += nums[i]

        return max(acc, cur)


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        array = []
        count = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                count += nums[i]
            else:
                array.append(count)
                count = nums[i]
        array.append(count)
        return max(array)


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        count = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                temp += nums[i]
            else:
                temp = nums[i]
            if count < temp:
                count = temp
        return count


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        temp = 0
        acc = 0
        for i in range(len(nums)):
            if i == 0 or nums[i-1] < nums[i]:
                temp += nums[i]
            else:
                temp = nums[i]
            if temp > acc:
                acc = temp
        return acc

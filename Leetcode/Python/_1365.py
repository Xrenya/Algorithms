class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Time complexity O(n)
        # Since unique numbers are limited [0-100] in the array 
        # we create a lenght of the array 102.
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, 102):
            count[i] += count[i-1]
        return [count[num] for num in nums]

def insertationSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while (i>-1) and (array[i]>key):
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key
    return array

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        array = nums
        temp = insertationSort(nums.copy())
        mapping = {}
        result = []
        for i in range(len(temp)):
            if temp[i] not in mapping:
                mapping[temp[i]] = i
        for i in range(len(nums)):
            result.append(mapping[nums[i]])
        return result

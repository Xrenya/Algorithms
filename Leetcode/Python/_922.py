class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        array = [None] * len(nums)
        odd = 1
        even = 0
        for num in nums:
            if num%2 == 0:
                array[even] = num
                even += 2
            else:
                array[odd] = num
                odd += 2
        return array
      
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        array = [None] * len(nums)
        odd = 1
        even = 0
        for num in nums:
            if num&1 == 0:
                array[even] = num
                even += 2
            else:
                array[odd] = num
                odd += 2
        return array

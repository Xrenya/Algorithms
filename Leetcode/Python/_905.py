class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 == 1:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
        

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        index = 0
        
        while index < len(A):
            num = A[index]
            
            if num % 2 == 0:
                even_num = A.pop(index)
                A.insert(0, even_num)
            
            index += 1
        return A
      
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        array_even = []
        array_odd = []
        for num in A:
            if num % 2 == 0:
                array_even.append(num)
            else:
                array_odd.append(num)
        return array_even + array_odd

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        array = []
        for num in A:
            if num % 2 == 0:
                array = [num] + array
            else:
                array.append(num)
        return array

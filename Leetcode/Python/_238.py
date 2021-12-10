class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        left_prefix = [1] * (lenght + 1)
        right_prefix = [1] * (lenght + 1)
        for i in range(1, lenght + 1):
            left_prefix[i] = left_prefix[i - 1] * nums[i - 1]
            right_prefix[lenght - i] = right_prefix[lenght - i + 1] * nums[lenght - i]
        output = []
        for i in range(lenght):
            output.append(left_prefix[i] * right_prefix[i + 1])
        return output

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_array=[]
        right_array=[]
        
        left_array.append(1)
        right_array.append(1)
        
        for i in range(1,len(nums)):
            
            left_array.append(left_array[-1] * nums[i-1])
            right_array.append(right_array[-1] * nums[len(nums) - i])
        
        return_array=[]
        
        for i in range(len(nums)):
            return_array.append(left_array[i]*right_array[len(nums)-1-i])
        
        return return_array

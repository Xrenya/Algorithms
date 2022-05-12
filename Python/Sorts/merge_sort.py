class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
        
        
    def buuble_sort(self, nums): # Time Limit Exceeded
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    
        return nums
    
    def bubble_sort_advanced(self, nums): # Time Limit Exceeded
        n = len(nums)

        for i in range(n):
            swapped = False

            for j in range(0, n - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True

            if swapped is False:
                break
                
        return nums
    
     
    def insertation_sort(self, nums): # Time Limit Exceeded
        for j in range(1, len(nums)):
            key = nums[j]
            i = j - 1
            while key < nums[i] and i > -1:
                nums[i + 1] = nums[i]
                i -= 1
            nums[i + 1] = key
        return nums
        
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        
        pivot = len(nums) // 2
        left = self.merge_sort(nums[:pivot])
        right = self.merge_sort(nums[pivot:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        l = r = 0
        output = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                output.append(left[l])
                l += 1
            else:
                output.append(right[r])
                r += 1
                
        output.extend(left[l:])
        output.extend(right[r:])
        
        
        return output

import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        return self.merge_sort(nums)

    def merge_sort(self, nums: List[int]) -> List[int]:
        # Select a pivot index
        # There is two ways to do it:
        # 1. Always select the middle pivot point: pivot = len(nums) // 2
        # 2. Select the random pivot point: pivot = random.randint(0, len(nums))
        if len(nums) <= 1:
            return nums
        pivot = len(nums) // 2
        left = self.merge_sort(nums[:pivot])
        right = self.merge_sort(nums[pivot:])
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        # case if one of the array is epmty we just return non-epmty array
        if not left and right:
            return right
        elif not right and left:
            return left

        left_pointer = 0
        right_pointer = 0
        
        merged_array = []
        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer] < right[right_pointer]:
                merged_array.append(left[left_pointer])
                left_pointer += 1
            else:
                merged_array.append(right[right_pointer])
                right_pointer += 1
        # case if one the array is finished and the oether is not finished
        merged_array.extend(left[left_pointer:])
        merged_array.extend(right[right_pointer:])
        return merged_array

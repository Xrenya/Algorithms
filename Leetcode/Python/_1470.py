class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = [0] * len(nums)
        for i in range(n):
            output[i * 2] = nums[i]
            output[i * 2 + 1] = nums[i + n]
        return output
    
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # n is middle point of the given array
        # nums - given array
        # Time complexity O(n)
        # Space compexity O(n)
        arr = []
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[n+i])
        return arr

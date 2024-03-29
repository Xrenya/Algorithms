class NumArray:

    def __init__(self, nums: List[int]):
        self.array = self.prefix(nums)

    def sumRange(self, left: int, right: int) -> int:
        return self.array[right + 1] - self.array[left]
        
    def prefix(self, nums):
        prefix = [0] * (len(nums) + 1)
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        return prefix


class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.prefixsum = self.get_prefix()

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixsum[right + 1] - self.prefixsum[left]
        
        
    def get_prefix(self):
        self.prefixsum = [0] * (len(self.array) + 1)
        for i in range(1, len(self.array) + 1):
            self.prefixsum[i] = self.prefixsum[i - 1] + self.array[i-1]
        return self.prefixsum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

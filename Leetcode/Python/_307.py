class NumArray:  
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = sum(nums)

    def update(self, index: int, val: int) -> None:
        self.sum -= self.nums[index]
        self.nums[index] = val
        self.sum += self.nums[index]

    def sumRange(self, left: int, right: int) -> int:
        if right - left > len(self.nums) // 2:
            temp = sum(self.nums[:left]) + sum(self.nums[right + 1:])
            return self.sum - (sum(self.nums[:left]) + sum(self.nums[right + 1:]))
        return sum(self.nums[left:right + 1])

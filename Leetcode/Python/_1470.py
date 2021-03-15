class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # n is middle point of the given array
        # nums - given array
        # Time complexity O(n)
        # Space compexity O(1)
        arr = []
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[n+i])
        return arr

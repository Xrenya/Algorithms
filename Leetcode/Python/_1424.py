class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        queue = [(0, 0)]
        output = []
        for row, col in queue:
            output.append(nums[row][col])
            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, col))

            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))

        return output

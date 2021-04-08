class Solution:    
    def countNegatives(self, grid: List[List[int]]) -> int:
        def countNegativeInRow(row: List[int]) -> int:
            left = 0
            right = len(row) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return len(row) - left
        
        count = 0
        for idx in range(len(grid)):
            count += countNegativeInRow(grid[idx])
        return count

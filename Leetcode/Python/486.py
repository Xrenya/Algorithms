class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(left, right):
            if left > right:
                return 0
            left_win = nums[left] - dfs(left + 1, right)
            right_win = nums[right] - dfs(left, right - 1)
            return max(left_win, right_win)
        return dfs(0, len(nums) - 1) >= 0

        
        def dfsNotOptimal(left, right, p1, p2, is_p1):
            if left > right:
                return p1 >= p2
            
            if is_p1:
                p1 += nums[left]
                is_true_left = dfs(left + 1, right, p1, p2, False)
                p1 -= nums[left]
                p1 += nums[right]
                is_true_right = dfs(left, right - 1, p1, p2, False)
                p1 -= nums[right]
                return is_true_left or is_true_right
            else:
                p2 += nums[left]
                is_true_left = dfs(left + 1, right, p1, p2, True)
                p2 -= nums[left]
                p2 += nums[right]
                is_true_right = dfs(left, right - 1, p1, p2, True)
                p2 -= nums[right]
                return is_true_left and is_true_right
        return dfs(0, len(nums) - 1) # dfs(0, len(nums) - 1, 0, 0, True)

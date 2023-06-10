class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def acc(index, value, n):
            count = 0

            if value > index:
                count += (value + value - index) * (index + 1) // 2
            else:
                count += (value + 1) * value // 2 + index - value + 1
 
            if value >= n - index:
                count += (value + value - n + 1 + index) * (n - index) // 2
            else:
                count += (value + 1) * value // 2 + n - index - value
            
            return count - value

        
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if acc(index, mid, n) <= maxSum:
                left = mid
            else:
                right = mid - 1
        
        return left
        

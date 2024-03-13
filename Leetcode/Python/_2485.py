class Solution:
    def pivotInteger(self, n: int) -> int:
        left_val = 1
        right_val = n
        sum_left = left_val
        sum_right = right_val

        if n == 1:
            return n

        while left_val < right_val:
            if sum_left < sum_right:
                sum_left += left_val + 1
                left_val += 1
            else:
                sum_right += right_val - 1
                right_val -= 1
            
            if sum_left == sum_right and left_val + 1 == right_val - 1:
                return left_val + 1

        return -1

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return x
        elif x < 4:
            return 1
        elif x < 9:
            return 2
        elif x < 16:
            return 3
        left = 0
        right = x // 3
        while left < right:
            middle = (left + right) // 2
            if middle * middle == x:
                return middle
            elif 0 < x - middle * middle < 2 * middle + 1:
                return middle
            elif middle * middle > x:
                right = middle
            else:
                left = middle + 1
                

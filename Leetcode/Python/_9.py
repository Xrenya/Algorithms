class Solution:
    def isPalindrome(self, x: int) -> bool:
        output = []
        if x < 0:
            return False
        elif x == 0:
            return True
        i = 0
        while x > 0:
            last_digit = x % 10
            if i == 0 and last_digit == 0:
                return False
            i += 1
            output.append(last_digit)
            x //= 10
            
        r = len(output) - 1
        l = 0
        while l < r:
            if output[l] == output[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
            

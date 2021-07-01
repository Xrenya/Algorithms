class Solution:
    def reverse(self, x: int) -> int:
        ans = []
        flag = False
        if x < 0:
            flag = True
            x *= (-1)
        while x > 0:
            last = x % 10
            x //= 10
            ans.append(last)
        output = 0
        for i, num in enumerate(ans[::-1]):
            output += num * 10**i
        if flag:
            output *= (-1)
        if output <= -2**31 or output >= 2**31 - 1:
            return 0
        return output

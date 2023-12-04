
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        output = ""
        cnt = 1
        prev = num[0]
        for n in num[1:]:
            if n == prev:
                cnt += 1
            elif cnt >= 3:
                cnt = 1
                if not output or int(output) < int(3 * prev):
                    output = prev * 3
                prev = n
            else:
                prev = n
                cnt = 1
        if cnt >= 3:
            if not output or int(output) < int(3 * prev):
                output = prev * 3
        return output

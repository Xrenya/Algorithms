class Solution:
    def calculate(self, s: str) -> int:
        queue = []
        cur_digit = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                cur_digit = cur_digit * 10 + int(s[i])
            if (not s[i].isdigit() and s[i] != " ") or i == len(s) - 1:
                if sign == "+":
                    queue.append(cur_digit)
                elif sign == "-":
                    queue.append(-cur_digit)
                elif sign == "*":
                    queue.append(queue.pop() * cur_digit)
                else:
                    temp = queue.pop()
                    if temp // cur_digit < 0 and temp % cur_digit != 0:
                        queue.append(temp // cur_digit + 1)
                    else:
                        queue.append(temp // cur_digit)
                sign = s[i]
                cur_digit = 0
        return sum(queue)

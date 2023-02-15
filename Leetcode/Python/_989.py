class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        n = len(num)
        output_sum = []
        for i in range(n - 1, -1, -1):
            add_digit = k % 10 if k else 0
            k //= 10
            summator = num[i] + add_digit + carry
            carry = summator // 10 % 10
            output_sum.append(summator % 10)
        while k:
            add_digit = k % 10
            k //= 10
            summator = add_digit + carry
            carry = summator // 10 % 10
            output_sum.append(summator % 10)
        if carry:
            output_sum.append(carry)
        return output_sum[::-1]

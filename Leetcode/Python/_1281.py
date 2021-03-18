class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        acc = 0
        mult = 1
        while n != 0:
            num = n % 10 
            n //= 10
            mult *= num
            acc += num
        return mult - acc

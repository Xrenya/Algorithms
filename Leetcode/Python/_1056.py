class Solution:
    def confusingNumber(self, n: int) -> bool:
        mapping = {0: 0, 1: 1, 6: 9, 9: 6, 8: 8}
        power = 0
        num = n
        number = []
        while n:
            last = n % 10
            if last in mapping:
                number.append(mapping[last])
            else:
                return False
            power += 1
            n //= 10
        revese = 0
        for i in range(len(number) - 1, -1, -1):
            revese +=  number[i] * (10 ** (len(number) - 1 - i))
        return revese != num

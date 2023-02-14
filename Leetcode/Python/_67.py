class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a

        b = b.zfill(len(a))
        print(a, b)
        carry = 0
        output = []
        for i in range(len(a) - 1, -1, -1):
            summator = int(a[i]) + int(b[i]) + carry
            output.append(1 if summator == 1 or summator == 3 else 0)
            if summator == 0 or summator == 1:
                carry = 0
            else:
                carry = 1
            print(summator, carry)
        if carry:
            output.append(carry)
        return "".join(map(str, output[::-1]))

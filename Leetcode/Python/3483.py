class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        visited = 0 << 1000
        output = 0

        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue

                for k in range(n):
                    if k == i or j == k or digits[k] % 2 != 0:
                        continue

                    x = digits[i] * 100 + digits[j] * 10 + digits[k]

                    if (visited & (1 << x)) == 0:
                        visited |= 1 << x
                        output += 1

        return output

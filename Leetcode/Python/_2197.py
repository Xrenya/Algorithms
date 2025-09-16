class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def find_gcd_euclidean(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def calculate_lcm(a, b, gcd_value):
            if a == 0 or b == 0:
                return 0
            else:
                return (a // gcd_value) * b

        output = []

        for num in nums:
            output.append(num)

            while len(output) >= 2:
                last = output.pop()
                prev = output.pop()
                gcd_value = find_gcd_euclidean(last, prev)
                if gcd_value > 1:
                    output.append(calculate_lcm(last, prev, gcd_value))
                else:
                    output.append(prev)
                    output.append(last)
                    break
        return output

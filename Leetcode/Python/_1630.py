?class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(a):
            min_el = min(a)
            max_el = max(a)

            if (max_el - min_el) % (len(a) - 1) != 0:
                return False

            d = (max_el - min_el) / (len(a) - 1)

            a_set = set(a)
            cur = min_el + d
            while cur < max_el:
                if cur not in a_set:
                    return False

                cur += d

            return True

        output = []
        for i in range(len(l)):
            a = nums[l[i]:r[i] + 1]
            output.append(check(a))

        return output

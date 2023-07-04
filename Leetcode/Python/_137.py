class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        left = 0

        for shift in range(32):
            bit_sum = 0
            for num in nums:
                bit_sum += (num >> shift) & 1

            left_bit = bit_sum % 3
            left = left | (left_bit << shift)

        if left >= (1 << 31):
            left = left - (1 << 32)

        return left

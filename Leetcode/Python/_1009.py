class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        # XOR n (n1) with a n2 which is all 1
        n1 = n
        num_bits = 0
        while n > 0:
            num_bits += 1
            n = n >> 1
        
        n2 = pow(2, num_bits) - 1
        return n1 ^ n2

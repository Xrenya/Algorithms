import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Helper function to count how many multiples exist <= max_val
        def count_multiples(max_val: int) -> int:
            total_count = 0
            # Iterate through all 2^n - 1 non-empty subsets using bitmasking
            for mask in range(1, 1 << n):
                current_lcm = 1
                subset_size = 0
                
                for i in range(n):
                    if (mask >> i) & 1:
                        subset_size += 1
                        # Compute LCM: (a * b) // gcd(a, b)
                        current_lcm = (current_lcm * coins[i]) // math.gcd(current_lcm, coins[i])
                        
                        # Optimization: If LCM exceeds max_val, its contribution is 0
                        if current_lcm > max_val:
                            break
                else:
                    # Inclusion-Exclusion Principle logic
                    multiples = max_val // current_lcm
                    if subset_size % 2 == 1:
                        total_count += multiples  # Odd size: add
                    else:
                        total_count -= multiples  # Even size: subtract
                        
            return total_count

        # Binary search range
        low = 1
        high = k * min(coins)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid       # mid is a valid candidate, try to find smaller
                high = mid - 1
            else:
                low = mid + 1   # Not enough multiples, look for a larger number
                
        return ans

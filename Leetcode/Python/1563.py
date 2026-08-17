import bisect
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        # Prefix sums for O(1) range sum queries
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        L = [[0] * n for _ in range(n)]
        R = [[0] * n for _ in range(n)]
        
        # Base cases for length 1
        for i in range(n):
            L[i][i] = pref[i+1]
            R[i][i] = -pref[i]
            
        # DP by subarray length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                target = pref[j+1] + pref[i]
                # Find the largest index `m` such that pref[m] <= target / 2
                m = bisect.bisect_right(pref, target / 2) - 1
                k = m - 1  # `k` is the split point where left_sum <= right_sum
                
                ans = 0
                
                # Case 1: left_sum < right_sum (split <= k)
                limit1 = min(k, j - 1)
                if limit1 >= i:
                    ans = max(ans, L[i][limit1] - pref[i])
                    
                # Case 2: left_sum > right_sum (split > k)
                limit2 = max(i, k + 1)
                if limit2 <= j - 1:
                    ans = max(ans, pref[j+1] + R[limit2 + 1][j])
                    
                # Case 3: left_sum == right_sum (happens exactly at split == k)
                if i <= k <= j - 1 and 2 * pref[k+1] == target:
                    ans = max(ans, pref[k+1] - pref[i] + max(dp[i][k], dp[k+1][j]))
                    
                dp[i][j] = ans
                
                # Update running maximums for L and R
                L[i][j] = max(L[i][j-1], pref[j+1] + dp[i][j])
                R[i][j] = max(R[i+1][j], dp[i][j] - pref[i])
                
        return dp[0][n-1]


class Solutionv1:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                
                max_score = 0
                for i in range(left, right):
                    left_sum = prefix[i + 1] - prefix[left]
                    right_sum = prefix[right + 1] - prefix[i + 1]
                    
                    if left_sum < right_sum:
                        max_score = max(max_score, left_sum + dp[left][i])
                    elif left_sum > right_sum:
                        max_score = max(max_score, right_sum + dp[i + 1][right])
                    else:
                        max_score = max(max_score, left_sum + max(dp[left][i], dp[i + 1][right]))
                        
                dp[left][right] = max_score
                
        return dp[0][n - 1]

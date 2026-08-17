import bisect
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        # pref[x] = sum of stoneValue[0:x]
        # Therefore, sum(i, j) = pref[j + 1] - pref[i]
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        # dp[i][j] = maximum score obtainable from interval [i, j]
        dp = [[0] * n for _ in range(n)]

        # L[i][j] = max(pref[k + 1] + dp[i][k]) for i <= k <= j
        #
        # This helps with cases where Alice keeps the LEFT part.
        L = [[0] * n for _ in range(n)]

        # R[i][j] = max(dp[k][j] - pref[k]) for i <= k <= j
        #
        # This helps with cases where Alice keeps the RIGHT part.
        R = [[0] * n for _ in range(n)]

        # Base case: a single stone cannot be split, so dp[i][i] = 0.
        for i in range(n):
            L[i][i] = pref[i + 1]       # pref[i + 1] + dp[i][i]
            R[i][i] = -pref[i]          # dp[i][i] - pref[i]

        # Build answers for intervals of increasing length.
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Total sum of interval [i, j]
                total = pref[j + 1] - pref[i]

                # We want to find a split k such that:
                #
                # left_sum = pref[k + 1] - pref[i]
                # right_sum = pref[j + 1] - pref[k + 1]
                #
                # left_sum <= right_sum means:
                # 2 * pref[k + 1] <= pref[i] + pref[j + 1]
                target = pref[i] + pref[j + 1]

                # m is the largest prefix index such that:
                # pref[m] <= target // 2
                #
                # Since m = k + 1, the split point is k = m - 1.
                m = bisect.bisect_right(pref, target // 2) - 1
                k = m - 1

                ans = 0

                # ----------------------------------------------------
                # Case 1: left_sum <= right_sum
                # Alice may keep the left interval [i, split].
                #
                # Score:
                # left_sum + dp[i][split]
                #
                # = (pref[split + 1] - pref[i]) + dp[i][split]
                #
                # = (pref[split + 1] + dp[i][split]) - pref[i]
                #
                # L[i][limit1] gives the best value of:
                # pref[split + 1] + dp[i][split]
                # ----------------------------------------------------
                limit1 = min(k, j - 1)

                if limit1 >= i:
                    ans = max(ans, L[i][limit1] - pref[i])

                # ----------------------------------------------------
                # Case 2: left_sum > right_sum
                # Alice must keep the right interval [split + 1, j].
                #
                # Score:
                # right_sum + dp[split + 1][j]
                #
                # = (pref[j + 1] - pref[split + 1])
                #   + dp[split + 1][j]
                #
                # = pref[j + 1]
                #   + (dp[split + 1][j] - pref[split + 1])
                #
                # R[start][j] stores the maximum value of:
                # dp[x][j] - pref[x]
                # for x >= start.
                # ----------------------------------------------------
                limit2 = max(i, k + 1)

                if limit2 <= j - 1:
                    ans = max(ans, pref[j + 1] + R[limit2 + 1][j])

                # ----------------------------------------------------
                # Case 3: left_sum == right_sum
                # Alice may choose either side.
                #
                # The left-side option is already included in Case 1.
                # Here we explicitly include the right-side option.
                # ----------------------------------------------------
                if i <= k <= j - 1 and 2 * pref[k + 1] == target:
                    equal_sum = pref[k + 1] - pref[i]
                    ans = max(
                        ans,
                        equal_sum + max(dp[i][k], dp[k + 1][j])
                    )

                dp[i][j] = ans

                # Update helper arrays after dp[i][j] is known.

                # Best left-side candidate ending at or before j
                L[i][j] = max(
                    L[i][j - 1],
                    pref[j + 1] + dp[i][j]
                )

                # Best right-side candidate starting at or after i
                R[i][j] = max(
                    R[i + 1][j],
                    dp[i][j] - pref[i]
                )

        return dp[0][n - 1]


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

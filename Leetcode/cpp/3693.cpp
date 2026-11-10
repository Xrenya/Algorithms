#include <iostream>
#include <climits>


class Solution {
public:
    int climbStairs(int n, std::vector<int>& costs) {
        std::vector<int> memo(n + 1, INT_MAX);
        memo[0] = 0;
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j < 4; ++j) {
                if (i - j < 0) {
                    continue;
                }
                memo[i] = std::min<int>(
                    memo[i],
                    memo[i - j] + costs[i - 1] + j * j
                );
            }
        }
        return memo.back();
    }
};

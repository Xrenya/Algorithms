#include <iostream>
#include <vector>
#include <cassert>
#include <climits>

class Solution {
public:
  int maxProfit(int k, std::vector<int>& prices) {
    int n = static_cast<int>(prices.size());
    if (n <= 0 || k <= 0) {
      return 0;
    }

    if (2 * k >= n) {
      int output = 0;
      for (int i = 1; i < n; ++i) {
        output += std::max<int>(0, prices[i] - prices[i - 1]);
      }
      return output;
    }

    // dp[i][used_k][is_hold] = balance
    // is_hold: 0 not_hold, 1 hold
    std::vector<std::vector<std::vector<int>>> dp(
      n, std::vector<std::vector<int>>(k + 1, std::vector<int>(2, 0))
    );
    // initialize the array with -inf
    // we use INT_MIN/2 here to prevent overflow
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j <= k; ++j) {
        dp[i][j][0] = INT_MIN / 2;
        dp[i][j][1] = INT_MIN / 2;
      }
    }

    dp[0][0][0] = 0;
    dp[0][1][1] = -prices[0];

    for (int i = 1; i < n; ++i) {
      for (int j = 0; j <= k; ++j) {
        // not holding
        dp[i][j][0] = std::max<int>(dp[i - 1][j][0],
            dp[i - 1][j][1] + prices[i]);
        // holding
        if (j > 0) {
          dp[i][j][1] = std::max<int>(
            dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i]
          );
        }
      }
    }
    int output = 0;
    for (int i = 0; i <= k; ++i) {
      output = std::max<int>(output, dp[n - 1][i][0]);
    }

    return output;
  }
};


int main() {
    Solution sol;
    std::vector<int> prices = {3, 2, 6, 5, 0, 3};
    int k = 2;
    int expected_output = 7;
    int output = sol.maxProfit(k, prices);
    assert(output == expected_output && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
}

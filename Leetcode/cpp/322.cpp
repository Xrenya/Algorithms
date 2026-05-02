#include <iostream>
#include <vector>
#include <cassert>
#include <string>
#include <climits>

class Solution {
public:
    int coinChange(std::vector<int>& coins, int amount) {
      std::vector<int> dp(amount + 1, INT_MAX / 2);
      dp[0] = 0;
      for (int i = 1; i <= amount; ++i) {
        for (auto coin : coins) {
          if (i - coin >= 0) {
            dp[i] = std::min(dp[i - coin] + 1, dp[i]);
          }
        }
      }
      return dp[amount] != INT_MAX / 2 ? dp[amount] : -1;
    }
};

int main() {
  Solution sol;
  std::vector<int> coins = {1, 2, 5};
  int amount = 11;
  int expected_output = 3;
  int output = sol.coinChange(coins, amount);
  assert ((output == expected_output) && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}

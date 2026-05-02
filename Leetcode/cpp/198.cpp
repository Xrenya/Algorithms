#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
  int rob(std::vector<int>& nums) {
    int n = static_cast<int>(nums.size());
    std::vector<int> dp(n + 2, 0);
    for (int i = 0; i < n; ++i) {
      dp[i + 2] = std::max(dp[i] + nums[i], dp[i + 1]);
    }
    return dp[n + 1];
  }
};

int main() {
  Solution sol;
  std::vector input = {1, 2, 3, 1};
  int expected_output = 4;
  
  int output = sol.rob(input);
  assert (output == expected_output && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}

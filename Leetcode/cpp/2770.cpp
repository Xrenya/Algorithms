#include <iostream>
#include <climits>
#include <cassert>
#include <vector>
#include <functional>

class Solution {
public:
  int maximumJumps(std::vector<int>& nums, int target) {
    int n = static_cast<int>(nums.size());
    std::vector<int> dp(n, INT_MIN);

    std::function<int(int)> dfs = [&](int i) -> int {
      if (i == n - 1) {
        return 0;
      }

      if (dp[i] != INT_MIN) {
        return dp[i];
      }
      int output = INT_MIN;
      for (int j = i + 1; j < n; ++j) {
        if (std::abs(nums[i] - nums[j]) <= target) {
          output = std::max<int>(output, dfs(j) + 1);
        }
      }
      return dp[i] = output;
    };
    int output = dfs(0);
    return output < 0 ? -1 : output;
  }
};

int main() {
  std::vector<int> nums = {1, 3, 6, 4, 1, 2};
  int target = 2;
  int expected_output = 3;
  Solution sol;
  int output = sol.maximumJumps(nums, target);
  
  assert ((expected_output == output) && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}

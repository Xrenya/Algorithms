#include <iostream>
#include <vector>
#include <cassert>
#include <string>
#include <climits>

class Solution {
public:
  int lengthOfLIS(std::vector<int>& nums) {
    int n = static_cast<int>(nums.size());
    std::vector<int> dp(n, 1);
    int max_len = 1;
    for (int i = 1; i < n; ++i) {
      for (int j = 0; j < i; ++j) {
        if (nums[i] > nums[j]) {
          dp[i] = std::max(dp[i], dp[j] + 1);
          max_len = std::max(max_len, dp[i]);
        }
      }
    }
    return max_len;
  }
};

int main() {
  Solution sol;
  std::vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
  int expected_output = 4;
  int output = sol.lengthOfLIS(nums);
  assert ((output == expected_output) && "Test #1 failed!");
  std::cout << "Tests are passed!" << std::endl;
  
  return 0;
}

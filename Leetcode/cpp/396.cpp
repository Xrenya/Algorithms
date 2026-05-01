#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>


class Solution {
 public:
  int maxRotateFunction(const std::vector<int>& nums) {
    const int n = static_cast<int>(nums.size());
    int64_t total = 0;
    int64_t current_sum = 0;

    for (int i = 0; i < n; ++i) {
      total += nums[i];
      current_sum += static_cast<int64_t>(nums[i]) * i;
    }

    long long max_value = current_sum;

    for (int i = 1; i < n; ++i) {
      current_sum += total - static_cast<int64_t>(nums[n - i]) * n;
      if (current_sum > max_value) {
        max_value = current_sum;
      }
    }

    return static_cast<int>(max_value);
  }
};

int main() {
  Solution sol;
  std::vector<int> input = {4, 3, 2, 6};
  int expected_output = 26;
  int output = sol.MaxRotateFunction(input);
  
  assert(expected_output == output && "Test #1 failed!");
  
  std::cout << "Tests are passed!" << std::endl;
  return 0;
}

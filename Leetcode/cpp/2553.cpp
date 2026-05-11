#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

class Solution {
public:
  std::vector<int> separateDigits(const std::vector<int>& nums) {
    std::vector<int> output;
    for (int i = nums.size() - 1; i >= 0; --i) {
      int num = nums[i];
      while (num > 0) {
        output.push_back(num % 10);
        num /= 10;
      }
    }
    std::reverse(output.begin(), output.end());
    return output;
  }

  std::vector<int> separateDigitsV1(const std::vector<int>& nums) {
    std::vector<int> output;
    for (auto num : nums) {
      std::vector<int> tmp;
      while (num > 0) {
        tmp.push_back(num % 10);
        num /= 10;
      }
      for (int i = tmp.size() - 1; i >= 0; --i) {
        output.push_back(tmp[i]);
      }
    }
    return output;
  }
};

int main() {
    Solution sol;
    std::vector<int> nums = {13, 25, 83, 77};
    std::vector<int> expected_otuput = {1, 3, 2, 5, 8, 3, 7, 7};
    std::vector<int> output = sol.separateDigitsV1(nums);
    assert ((output == expected_otuput) && "Test #1 failed!");
    
    output = sol.separateDigits(nums);
    assert ((output == expected_otuput) && "Test #2 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}

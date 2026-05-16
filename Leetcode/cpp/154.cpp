#include <iostream>
#include <vector>
#include <cassert>


class Solution {
public:
    int findMin(std::vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        int left = 0;
        int right = n - 1;
        while (left < right) {
          int m = left + (right - left) / 2;
          if (nums[m] < nums[right]) {
            right = m;
          } else if (nums[m] > nums[right]) {
            left = m + 1;
          } else {
            right -= 1;
          }
        }
        return std::min(nums[0], nums[left]);
        
    }
};

int main() {
    Solution sol;
    std::vector<int> nums = {3, 4, 1, 3};
    int expected_output = 1;
    int output = sol.findMin(nums);
    
    assert((expected_output == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}

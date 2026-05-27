#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>

class Solution {
public:
    int firstMissingPositive(std::vector<int>& nums) {
        int n = nums.size();
      
        for (int i = 0; i < n; ++i) {
            while (nums[i] > 0 && nums[i] <= n && nums[i] != nums[nums[i] - 1]) {
                std::swap(nums[i], nums[nums[i] - 1]);
            }
        }
      
        for (int i = 0; i < n; ++i) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
      
        return n + 1;
    }
};

int main() {
    Solution sol;
    std::vector<int> nums = {1, 2, 0};
    int expextedOutput = 3;
    int output = sol.firstMissingPositive(nums);
    assert((expextedOutput == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}

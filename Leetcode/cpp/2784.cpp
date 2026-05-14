#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

class Solution {
public:
    bool isGood(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = static_cast<int>(nums.size()) - 1;
        for (int i = 0; i < n; ++i) {
            if (nums[i] != i + 1) {
                return false;
            }
        }
        return nums[n] == n;
    }
};


int main() {
    Solution sol;
    std::vector<int> nums = {1, 3, 3, 2};
    bool expected_output = true;
    bool output = sol.isGood(nums);
    
    assert ((expected_output == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}

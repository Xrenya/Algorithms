#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    bool check(std::vector<int>& nums) {
        bool sorted = true;
        bool first = false;
        int index = -1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i - 1] <= nums[i]) {
                continue;
            } else {
                if (!first) {
                    first = true;
                } else if (first) {
                    return false;
                }
            }
        }
        if (first) {
            if (nums[nums.size() - 1] <= nums[0]) {
                return true;
            }
            return false;
        }
        return true;
    }
};

int main() {
    Solution sol;
    std::vector nums = {1, 2, 3, 4};
    bool expected_output = true;
    bool output = sol.check(nums);
    assert((expected_output == output) && "Test #1 failed!");
    
    
    nums = {4, 5, 1, 2, 3, 4};
    expected_output = true;
    output = sol.check(nums);
    assert((expected_output == output) && "Test #2 failed!");
    
    nums = {4, 7, 5, 1, 2, 3, 4};
    expected_output = false;
    output = sol.check(nums);
    assert((expected_output == output) && "Test #3 failed!");
    
    nums = {1, 1, 1};
    expected_output = true;
    output = sol.check(nums);
    assert((expected_output == output) && "Test #4 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}

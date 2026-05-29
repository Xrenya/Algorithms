#include <iostream>
#include <vector>
#include <cassert>
#include <climits>

class Solution {
public:
    int minElement(std::vector<int>& nums) {
        int minNum = INT_MAX;
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            int num = nums[i];
            int acc = 0;
            while (num) {
                acc += num % 10;
                num /= 10;
            }
            if (minNum > acc) {
                minNum = acc;
            }
        }
        return minNum;
    }
};


int main() {
    Solution sol;
    std::vector<int> nums = {10, 12, 13, 14};
    int expectedOutput = 1;
    int output = sol.minElement(nums);
    
    assert((expectedOutput == output) && "Test #1 failed!");
    
    nums = {15, 12, 13, 14};
    expectedOutput = 3;
    output = sol.minElement(nums);
    
    assert((expectedOutput == output) && "Test #2 failed!");
    
    std::cout << "All tests are passed!" << std::endl;
    
    return 0;
}

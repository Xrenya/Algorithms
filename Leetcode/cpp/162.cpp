#include <iostream>
#include <vector>
#include <cassert>


class Solution {
public:
    int findPeakElement(std::vector<int>& nums) {
        int val = nums[0], index = 0;
        for (int i = 1; i < nums.size() - 1; ++i) {
            if (val < nums[i] && nums[i] > nums[i + 1]) {
                return i;
            }
        }
        if (nums.size() >= 2 && nums[nums.size() - 1] > nums[nums.size() - 2]) {
            return (int) nums.size() - 1;
        }
        return index;
    }
};

int main()
{
    Solution sol;
    std::vector<int> input = {1,2,3,1};
    int expected_output = 2;
    int output = sol.findPeakElement(input);
    
    assert(expected_output == output && "Test #1 failed");
    
    input = {2,3};
    expected_output = 1;
    output = sol.findPeakElement(input);
    assert(expected_output == output && "Test #2 failed");

    std::cout << "Tests are passed!" << std::endl;
    return 0;
}

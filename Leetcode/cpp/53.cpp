#include <iostream>
#include <vector>
#include <cassert>


class Solution {
public:
    int maxSubArray(std::vector<int>& nums) {
        int max = nums[0], cur = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            cur = std::max(nums[i], cur + nums[i]);
            max = std::max(cur, max);
        }
        return max;
    }
};
int main()
{
    std::vector<int> data = {-2,1,-3,4,-1,2,1,-5,4};
    int expected_output = 6;
    Solution sol;
    int output = sol.maxSubArray(data);


    assert(expected_output == output && "Test #1 failed");

    std::cout << "Tests are passed!" << std::endl;
    return 0;
}


#include <iostream>
#include <vector>
#include <cassert>


class Solution {
public:
    int maxSubarraySumCircular(std::vector<int>& nums) {
        int max_sum = nums[0];
        int cur_max = 0;
        int min_sum = nums[0];
        int cur_min = 0;
        int total = 0;
        for (int i = 0; i < nums.size(); ++i) {
            cur_max = std::max(nums[i], cur_max + nums[i]);
            max_sum = std::max(max_sum, cur_max);

            cur_min = std::min(nums[i], cur_min + nums[i]);
            min_sum = std::min(cur_min, min_sum);

            total += nums[i];
        }

        if (total == min_sum) {
            return max_sum;
        }
        return std::max(max_sum, total - min_sum);
    }
};

int main()
{
    Solution sol;
    std::vector<int> input = {1,-2,3,-2};
    int expected_output = 3;
    int output = sol.maxSubarraySumCircular(input);
    
    assert(expected_output == output && "Test #1 failed");
    
    input = {-3,-2,-3};
    expected_output = -2;
    output = sol.maxSubarraySumCircular(input);
    assert(expected_output == output && "Test #2 failed");

    std::cout << "Tests are passed!" << std::endl;
    return 0;
}

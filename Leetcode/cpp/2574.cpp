#include <iostream>
#include <vector>
#include <cassert>

class Solution {
public:
    std::vector<int> leftRightDifference(std::vector<int>& nums) {
        // auto pprint = [](const std::vector<int>& a) {
        //     for (size_t i = 0; i < a.size(); ++i) {
        //         std::cout << a[i] << " ";
        //     }
        //     std::cout << std::endl;
        // };
        int n = static_cast<int>(nums.size());
        std::vector<int> left(n, 0);
        std::vector<int> right(n, 0);
        for (int i = 1; i < n; ++i) {
            left[i] = left[i - 1] + nums[i - 1];
        }
        // pprint(left);
        for (int i = n - 2; i >= 0; --i) {
            right[i] = right[i + 1] + nums[i + 1];
        }
        // pprint(right);

        std::vector<int> output(n, 0);
        for (int i = 0; i < n; ++i) {
            output[i] = std::abs(right[i] - left[i]);
        }
        return output;
    }
};

int main() {
    Solution sol;
    std::vector<int> nums = {10, 4, 8, 3};
    std::vector<int> expectedOutput = {15, 1, 11, 22};
    
    std::vector<int> output = sol.leftRightDifference(nums);
    
    assert((output == expectedOutput) && "Test #1 failed!");
    
    std::cout << "Tests are passed!" << std::endl;
    
    return 0;
}

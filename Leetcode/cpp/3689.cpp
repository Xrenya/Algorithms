#include <iostream>
#include <vector>
#include <cassert>
#include <climits>

class Solution {
public:
    long long maxTotalValue(std::vector<int>& nums, int k) {
        long long max = 0, min = INT_MAX;
        for (auto num : nums) {
            max = std::max<int>(max, num);
            min = std::min<int>(min, num);
        }
        return (max - min) * k;
    }
};

int main() {
    Solution sol;
    std::vector<int> nums = {1, 3, 2};
    int k = 2;
    long long expectedOutput = 4;
    long long output = sol.maxTotalValue(nums, k);
    assert((expectedOutput == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}

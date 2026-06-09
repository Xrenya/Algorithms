#include <iostream>
#include <vector>
#include <cassert>
#include <climits>

class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        long long max = LLONG_MIN, min = LLONG_MAX;
        for (auto num : nums) {
            max = std::max<long long>(max, num);
            min = std::min<long long>(min, num);
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

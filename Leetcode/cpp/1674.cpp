#include <iostream>
#include <cassert>
#include <vector>

class Solution {
public:
    int minMoves(std::vector<int>& nums, int limit) {
        int n = static_cast<int>(nums.size());
        std::vector<int> diff(2 * limit + 2, 0);

        for (int i = 0; i < n / 2; ++i) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            diff[2] += 2;
            diff[std::min<int>(a, b) + 1] -= 1;
            diff[a + b] -= 1;
            diff[a + b + 1] += 1;
            diff[std::max<int>(a, b) + limit + 1] += 1;
        }

        int output = n;
        int current = 0;
        for (int i = 2; i < 2 * limit + 1; ++i) {
            current += diff[i];
            output = std::min<int>(output, current);
        }
        return output;
    }
};

int main() {
    Solution sol;
    std::vector<int> nums = {1, 2, 4, 3};
    int limit = 4;
    int expected_output = 1;
    int output = sol.minMoves(nums, limit);
    
    assert ((expected_output == output) && "Test #1 failed!");
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}

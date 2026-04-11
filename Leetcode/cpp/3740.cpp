#include <iostream>
#include <vector>
#include <cassert>


class Solution {
public:
    int minimumDistances(std::vector<int>& nums) {
        int n = nums.size();
        int output = n + 1;

        for (int i = 0; i < n - 2; ++i) {
            for (int j = i + 1; j < n - 1; ++j) {
                if (nums[i] != nums[j]) continue;
                for (int k = j + 1; k < n; ++k) {
                    if (nums[k] == nums[j]) {
                        output = std::min(output, k - i);
                        break;
                    }
                }
            }
        } 
        return (output == n + 1) ? -1 : output * 2;
    }
};


int main() {
    Solution sol;
    int expected_output = 6;
    std::vector<int> nums = {1,2,1,1,3};
    int output = sol.minimumDistances(nums);
    assert (output == expected_output), "Output is not equal to expected_output";
    std::cout << "Test is passed!" << std::endl;

    return 0;
}

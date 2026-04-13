#include <iostream>
#include <climits>
#include <vector>
#include <cassert>

class Solution {
public:
    int getMinDistance(std::vector<int>& nums, int target, int start) {
        int m = INT_MAX;
        for (int i = 0; i < nums.size(); ++i) {
            if (target == nums[i] && m > abs(start - i)) {
                m = abs(start - i);
            }
        }
        return m;
    }
};

int main()
{
    Solution sol;
    int expected_output = 1, target = 5, start = 3;
    std::vector<int> nums = {1,2,3,4,5};
    assert (expected_output == sol.getMinDistance(nums, target, start));
    std::cout << "Test is passed" << std::endl;

    return 0;
}

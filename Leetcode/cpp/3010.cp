#include <iostream>
#include <vector>


class Solution {
public:
    int minimumCost(std::vector<int>& nums) {
        int a = 51, b = 51;
        for (std::vector<int>::size_type i = 1; i < nums.size(); ++i) {
            if (nums[i] < a) {
                b = a;
                a = nums[i];
            } else if (nums[i] < b) {
                b = nums[i];
            }

            if (a == 1 && b == 1) {
                break;
            }
        }
        return nums[0] + a + b;
    }
};

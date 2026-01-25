#include <iostream>
#include <vector>


class Solution {
public:
    int minimumDifference(std::vector<int>& nums, int k) {
        if (k <= 0) {return 0;}
        std::sort(nums.begin(), nums.end());
        int minDif = INT_MAX;
        for (std::vector<int>::size_type i = 0; i + k - 1< nums.size(); ++i) {
            minDif = std::min(minDif, nums[i + k - 1] - nums[i]);
        }
        return minDif;
    }
};

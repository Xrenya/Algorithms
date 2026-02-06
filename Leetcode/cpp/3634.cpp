#include <iostream>
#include <algorithm>
#include <vector>

class Solution {
public:
    int minRemoval(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int size = nums.size();
        int output = size;
        int right = 0;
        for (int left = 0; left < size; ++left) {
            while (right < size && nums[right] <= static_cast<long long>(nums[left]) * k) {
                ++right;
            }
            output = std::min(output, size - (right - left));
        }
        return output;
    }
};

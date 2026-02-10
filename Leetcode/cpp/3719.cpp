#include <iostream>
#include <vector>
#include <unordered_map>


class Solution {
public:
    int longestBalanced(std::vector<int>& nums) {
        std::vector<int>::size_type len = 0;
        
        for (std::vector<int>::size_type i = 0; i < nums.size(); ++i) {
            auto odd = std::unordered_map<int, int>();
            auto even = std::unordered_map<int, int>();

            for (std::vector<int>::size_type j = i; j < nums.size(); ++j) {
                auto& c = (nums[j] & 1) ? odd : even;
                ++c[nums[j]];

                if (odd.size() == even.size()) {
                    len = std::max(len, j - i + 1);
                }
            }
        }
        return static_cast<int>(len);
    }
};

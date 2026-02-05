#include <iostream>
#include <vector>

class Solution {
public:
    std::vector<int> constructTransformedArray(std::vector<int>& nums) {
        int size = nums.size();
        std::vector<int> result(size);
        for (int i = 0; i < size; ++i) {
            result[i] = nums[((i + nums[i]) % size + size) % size];
        }
        return result;
    }
};

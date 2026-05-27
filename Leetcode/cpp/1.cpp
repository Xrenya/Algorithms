#include <iostream>
#include <unordered_map>
#include <set>
#include <cassert>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(const std::vector<int>& nums, const int& target) {
        std::unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); ++i) {
            if (hash.contains(target - nums[i])) {
                return {hash[target - nums[i]], i};
            }
            hash[nums[i]] = i;
        }
        return {-1, -1};
    }
};

int main() {
    Solution sol;
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> expectedOutput = {0, 1};
    
    std::vector<int> output = sol.twoSum(nums, target);
    assert((expectedOutput == output) && "Test #1 failed!");
    
    std::cout << "All tests are passed!" << std::endl;
    return 0;
}

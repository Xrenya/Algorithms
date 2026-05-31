#include <iostream>
#include <vector>
#include <cassert>
#include <unordered_map>

class Solution {
public:
    int minSubarray(std::vector<int>& nums, int p) {
        int n = static_cast<int>(nums.size());
        int total_reminder = 0;
        for (int& num : nums) {
            total_reminder = (total_reminder + num) % p;
        }

        if (total_reminder % p == 0) {
            return 0;
        }

        std::unordered_map<int, int> lastIndexMap;
        lastIndexMap[0] = -1;
        int current = 0;
        int minLength = n;

        for (int i = 0; i < n; ++i) {
            current = (current + nums[i]) % p;

            int targetRemainder  = (current - total_reminder + p) % p;
            if (lastIndexMap.count(targetRemainder)) {
                minLength = std::min(minLength, i - lastIndexMap[targetRemainder ]);
            }
          
            lastIndexMap[current] = i;
        }
      
        return minLength == n ? -1 : minLength;

    }
};

int main() {
    Solution sol;
    std::vector<int> nums = {3, 1, 4, 2};
    int p = 6;
    int expectedOutput = 1;
    int output = sol.minSubarray(nums, p);
    assert((expectedOutput == output) && "Test #1 failed!");
    std::cout << "Tests are passsed!" << std::endl;
    return 0;
}

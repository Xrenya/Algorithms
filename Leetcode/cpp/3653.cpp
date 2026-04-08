#include <iostream>
#include <vector>
#include <cassert>


class Solution {
    static const  int mod = 1e9 + 7;

public:
    int xorAfterQueries(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = nums.size();
        for (auto q : queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            for (int i = l; i <= r; i += k) {
                nums[i] = 1ll * nums[i] * v % mod;
            }
        }
        int res = 0;
        for (auto n : nums) {
            res ^= n;
        }
        return res;
    }
};


int main()
{
    std::vector<int> nums = {1, 1, 1};
    std::vector<std::vector<int>> queries = { {0, 2, 1, 4} };
    int expected_output = 4;
    Solution sol;
    
    int res = sol.xorAfterQueries(nums, queries);
    assert (res == expected_output);
    std::cout << "Test is passed!" << std::endl;
    return 0;
}

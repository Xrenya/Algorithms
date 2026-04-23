#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <unordered_map>

class Solution {
public:
    std::vector<long long> distance(std::vector<int>& nums) {
        int n = (int) nums.size();
        std::vector<long long> ans(n, 0);

        std::unordered_map<int, long long> cnt, sum;
        cnt.reserve(n * 2);
        sum.reserve(n * 2);

        // left to right: distance to previous same values
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            ans[i] += 1LL * cnt[x] * i - sum[x];
            cnt[x] += 1;
            sum[x] += i;
        }

        // right to left: distance to next same values
        cnt.clear();
        sum.clear();
        cnt.reserve(n * 2);
        sum.reserve(n * 2);

        for (int i = n - 1; i >= 0; --i) {
            int x = nums[i];
            ans[i] += sum[x] - 1LL * cnt[x] * i;
            cnt[x] += 1;
            sum[x] += i;
        }

        return ans;
    }
};

int main(void) {
    Solution sol;
    std::vector<int> input = {1,3,1,1,2};
    std::vector<long long> expected_output = {5,0,3,4,0};
    std::vector<long long> output = sol.distance(input);
    for (int i = 0; i < output.size(); ++i) {
        assert ((expected_output[i] == output[i]) &&  ("Test failed at index " + std::to_string(i)).c_str());   
    }
    std::cout << "Tests are passed!" << std::endl;
    return 0;
}

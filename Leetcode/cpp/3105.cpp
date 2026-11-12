class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int dec = 1;
        int inc = 1;
        int cur = 1;
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] > nums[i + 1]) {
                ++dec;
                inc = 1;
            } else if (nums[i] < nums[i + 1]) {
                ++inc;
                dec = 1;
            } else {
                dec = 1;
                inc = 1;
            }
            cur = std::max<int>(cur, std::max<int>(inc, dec));
        }
        return cur;
    }
};

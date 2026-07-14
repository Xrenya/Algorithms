class Solution {
public:
    int jumpDP(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> dp(n, INT_MAX);
        dp[n - 1] = 0;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = 1; j <= nums[i]; ++j) {
                int index = std::min<int>(n - 1, j + i);
                if (dp[index] != INT_MAX) {
                    dp[i] = std::min<int>(dp[i], dp[index] + 1);
                }
            }
        }
        return dp[0];
    }
    int jump(vector<int>& nums) {
        int cur_pos = 0;
        int max_jump_pos = 0;
        int min_jumps = 0;
        for (int i = 0; i < nums.size() - 1; ++i) {
            max_jump_pos = std::max<int>(max_jump_pos, i + nums[i]);
            if (i == cur_pos) {
                ++min_jumps;
                cur_pos = max_jump_pos;
            }
        }
        return min_jumps;
    }
};

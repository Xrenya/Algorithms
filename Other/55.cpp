class Solution {
public:
    void dfs(int position, vector<int>& nums, vector<int>& dp) {
        if (position >= nums.size()) {
            return; 
        }
        dp[position] = 1;
        for (int i = nums[position]; i >= 1; --i) {
            if (position + i < nums.size() && dp[position + i] == -1) {
                dfs(position + i, nums, dp);
            }
        }

    }

    bool canJumpDP(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> dp(n + 1, -1);
        dfs(0, nums, dp);
        // for (int i = 0; i < n; ++i) {
        //     std::cout << dp[i] << " ";
        // }
        return dp[n - 1] == 1;
    }

    bool canJump(vector<int>& nums) {
        int n = nums.size() - 1;
        int index = n;
        for (int i = n; i >= 0; --i) {
            if (nums[i] + i >= index) {
                index = i;
            }
        }
        return index == 0;
    }
};

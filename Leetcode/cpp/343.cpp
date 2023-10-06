class Solution {
public:
    int integerBreak(int n) {
        if (n <= 3) {
            return n - 1;
        }
        vector<int> dp(n + 1);

        for (int i = 0; i < 4; i++) {
            dp[i] = i;
        }

        for (int j = 4; j <= n; j++) {
            int ans = j;
            for (int i = 0; i < j; i++) {
                ans = std::max(ans, i * dp[j - i]);
            }
            dp[j] = ans;
        }
        return dp[n];
    }
};

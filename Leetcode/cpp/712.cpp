#include <iostream>
#include <algorithm>
#include <vector>

class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int m = s1.size();
        int n = s2.size();

        // dp[i][j] = min delete sum to make s1[0..i-1] and s2[0..j-1] equal
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));

        // If s2 is empty, delete all chars from s1
        for (int i = 1; i <= m; ++i) {
            dp[i][0] = dp[i - 1][0] + s1[i - 1];
        }

        // If s1 is empty, delete all chars from s2
        for (int j = 1; j <= n; ++j) {
            dp[0][j] = dp[0][j - 1] + s2[j - 1];
        }

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = min(
                        s1[i - 1] + dp[i - 1][j],
                        s2[j - 1] + dp[i][j - 1]
                    );
                }
            }
        }

        return dp[m][n];
    }
};
/* another version*/
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <string>

class Solution {
public:
    // memo[key] where key encodes (ptr1, ptr2)
    std::unordered_map<long long, int> umap;

    // Encode (ptr1, ptr2) into a single 64-bit integer.
    // Shift by +1 so that -1 becomes 0, 0 -> 1, etc.
    long long makeKey(int ptr1, int ptr2) const {
        long long a = static_cast<long long>(ptr1) + 1;
        long long b = static_cast<long long>(ptr2) + 1;
        return (a << 32) ^ b;
    }

    int computeCost(const string &s1, const string &s2, int ptr1, int ptr2) {
        if (ptr1 < 0 && ptr2 < 0) {
            return 0;
        }

        long long key = makeKey(ptr1, ptr2);
        auto it = umap.find(key);
        if (it != umap.end()) {
            return it->second;
        }

        int res;
        if (ptr1 < 0) {
            res = s2[ptr2] + computeCost(s1, s2, ptr1, ptr2 - 1);
        } else if (ptr2 < 0) {
            res = s1[ptr1] + computeCost(s1, s2, ptr1 - 1, ptr2);
        } else if (s1[ptr1] == s2[ptr2]) {
            res = computeCost(s1, s2, ptr1 - 1, ptr2 - 1);
        } else {
            res = min(
                s1[ptr1] + computeCost(s1, s2, ptr1 - 1, ptr2),
                s2[ptr2] + computeCost(s1, s2, ptr1, ptr2 - 1)
            );
        }

        umap[key] = res;
        return res;
    }

    int minimumDeleteSum(string s1, string s2) {
        umap.clear();
        return computeCost(s1, s2, (int)s1.size() - 1, (int)s2.size() - 1);
    }
};

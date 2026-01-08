#include <vector>
#include <climits>
#include <algorithm>

class Solution {
public:
    vector<vector<std::optional<int>>> memo;
    vector<vector<bool>> visited;

    int dp(int i, int j, vector<int>& nums1, vector<int>& nums2) {
        if (i == nums1.size() || j == nums2.size()) {
            return 0;
        }
        if (visited[i][j]) {
            if (memo[i][j].has_value()) return *memo[i][j];
        }

        int use = nums1[i] * nums2[j] + dp(i + 1, j + 1, nums1, nums2);
        int result = std::max(use, std::max(dp(i + 1, j, nums1, nums2), dp(i, j + 1, nums1, nums2)));

        memo[i][j] = result;
        visited[i][j] = true;
        return result;
    }

    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int firstMax = *std::max_element(nums1.begin(), nums1.end());
        int firstMin = *std::min_element(nums1.begin(), nums1.end());
        int secondMax = *std::max_element(nums2.begin(), nums2.end());
        int secondMin = *std::min_element(nums2.begin(), nums2.end());

        if (firstMax < 0 && secondMin > 0) {
            return firstMax * secondMin;
        }
        if (firstMin > 0 && secondMax < 0) {
            return firstMin * secondMax;
        }

        memo = std::vector(nums1.size(), std::vector<std::optional<int>>(nums2.size(), 0));
        visited = std::vector(nums1.size(), std::vector<bool>(nums2.size(), false));
        return dp(0, 0, nums1, nums2);
    }
};

class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size();
        std::vector<int> suffix(n, 0);
        suffix[n - 1] = nums.back();
        for (int i = n - 2; i >= 0; --i) {
            suffix[i] = std::min<int>(suffix[i + 1], nums[i]);
        }
        int cmax = nums[0];
        for (int j = 0; j < n; ++j) {
            cmax = std::max<int>(cmax, nums[j]);
            int dist = cmax - suffix[j];
            if (dist <= k) {
                return j;
            }
        }
        return -1;
    }
};

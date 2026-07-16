class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        std::sort(nums.begin(), nums.end());
        int len = 1;
        int tmp = 1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] - 1 == nums[i - 1]) {
                ++tmp;
            } else if (nums[i] == nums[i - 1]) {
                continue;
            } else {
                tmp = 1;
            }
            len = std::max<int>(len, tmp);
        }
        return len;
    }
};

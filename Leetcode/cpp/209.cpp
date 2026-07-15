class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int minSize = nums.size() + 1;
        int j = 0;
        int acc = 0;
        for (int i = 0; i < nums.size(); ++i) {
            acc += nums[i];
            while (acc >= target) {
                if (acc >= target) {
                    minSize = std::min<int>(minSize, i - j + 1);
                }
                acc -= nums[j++];
            }
        }
        return (minSize == nums.size() + 1) ? 0 : minSize;
    }
};

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int prev = nums[0];
        int index = 0;
        int k = 1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] == prev) {
                ++k;
                if (k <= 2) {
                    nums[++index] = nums[i];
                }
            } else {
                k = 1;
                prev = nums[i];
                nums[++index] = nums[i];
            }
        }
        return index + 1;
    }
};

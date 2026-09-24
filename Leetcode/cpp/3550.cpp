class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        for (int i = 0; i < nums.size(); ++i) {
            int val = nums[i];
            int cur = 0;
            while (val > 0) {
                cur += (val % 10);
                val /= 10;
            }
            if (cur == i) {
                return i;
            }
        }
        return -1;
    }
};

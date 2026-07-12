class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int val = INT_MAX;
        for (int i = 0; i < nums.size(); ++i) {
            if (val == nums[i]) {
                ++count;
            } else if (val != nums[i]) {
                --count;
                if (count <= 0) {
                    count = 1;
                    val = nums[i];
                } else if (count / 2 + 1  > nums.size()) {
                    return val;
                }
            }
        }
        return val;
    }
};

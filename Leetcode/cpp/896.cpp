class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool increase = true, decrease = true;
        for (int i = 1; i < nums.size(); i++){
            if (nums[i - 1] < nums[i]) {
                decrease = false;
            } else if (nums[i - 1] > nums[i]) {
                increase = false;
            }
        }
        return increase || decrease;
    }
};

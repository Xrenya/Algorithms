class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = -1, right = nums.size();
        while (left < right - 1) {
            int m = left + (right - left) / 2;
            if (nums[m] <= target) {
                left = m;
            } else {
                right = m;
            }
        }
        return left >=0 && left < nums.size() && nums[left] == target  ? left: -1;
    }
};

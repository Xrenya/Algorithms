class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = -1;
        int r = nums.size();
        int mid;
        while (l < r - 1){
            mid = l + (r - l) / 2;
            if (nums[mid] == target){
                return mid;
            }
            else{
                if (nums[mid] > target){
                    r = mid;
                }
                else{
                    l = mid;
                }
            }
        }
        return r;
    }
};

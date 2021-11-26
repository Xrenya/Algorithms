class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        int l = -1;
        int r = n;
        while(l < r - 1){
            int mid = (l + r) >> 1;
            if(nums[mid] == target){
                return mid;
            }
            else if(nums[mid] < target){
                 l = mid;
            }
            else if(nums[mid] > target){
                r = mid;
            }
        }
        return r;
    }
};

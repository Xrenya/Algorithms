class Solution {
public:
    void twoSum(int index, std::vector<int>& nums, std::vector<std::vector<int>>& output) {
        int left = index + 1;
        int right = nums.size() - 1;
        while (left < right) {
            int target = nums[index] + nums[left] + nums[right];
            if (target > 0) {
                --right;
            } else if (target < 0) {
                ++left;
            } else {
                output.push_back({nums[index], nums[left], nums[right]});
                ++left;
                --right;
                while (left < right && nums[left] == nums[left - 1]) {
                    ++left;
                }
            }
        }
    }

    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> output;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) {
                break;
            } else if (i == 0 || nums[i - 1] != nums[i]) {
                twoSum(i, nums, output);
            }
        }
        return output;
    }
};

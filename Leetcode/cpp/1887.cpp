class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int output = 0, up = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i - 1]) {
                up += 1;
            }
            output += up;
        }
        return output;
    }
};

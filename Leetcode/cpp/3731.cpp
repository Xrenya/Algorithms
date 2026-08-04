class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        if (nums.empty()) {
            return {};
        }
        std::sort(nums.begin(), nums.end());
        std::vector<int> output;
        int index = 0;
        for (int i = nums[0]; i <= nums.back(); ++i) {
            if (index < nums.size() && nums[index] == i) {
                ++index;
            } else {
                output.push_back(i);
            }
        }
        return output;
    }
};

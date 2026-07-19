class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        std::vector<std::vector<int>> output;
        std::function<void(int)> dfs = [&](int index) -> void {
            if (index == nums.size()) {
                output.push_back(nums);
                return;
            }
            for (int i = index; i < nums.size(); ++i) {
                std::swap(nums[index], nums[i]);
                dfs(index + 1);
                std::swap(nums[index], nums[i]);
            }
        };
        dfs(0);
        return output;
    }
};

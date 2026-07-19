class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        std::vector<std::vector<int>> output;
        std::function<void(int, int, std::vector<int>&)> dfs = [&](int index, int cur, std::vector<int>& tmp) -> void {
            if (cur == target) {
                output.push_back(tmp);
                return;
            }
            if (index == candidates.size() || cur > target) {
                return;
            }
            tmp.push_back(candidates[index]);
            cur += candidates[index];
            dfs(index, cur, tmp);
            cur -= candidates[index];
            tmp.pop_back();

            dfs(index + 1, cur, tmp);
            return;
        };
        std::vector<int> tmp;
        dfs(0, 0, tmp);
        return output;
    }
};

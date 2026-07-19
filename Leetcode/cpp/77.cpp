class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        std::vector<std::vector<int>> output;
        std::function<void(std::vector<int>&, int)> dfs = [&](std::vector<int>& tmp, int index) -> void {
            if (tmp.size() == k) {
                output.push_back(tmp);
                return;
            }
            for (int i = index; i <= n; ++i) {
                tmp.push_back(i);
                dfs(tmp, i + 1);
                tmp.pop_back();
            }
        };
        std::vector<int> tmp;
        dfs(tmp, 1);
        return output;
    }
};

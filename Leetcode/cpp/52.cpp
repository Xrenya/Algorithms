class Solution {
public:
    int totalNQueens(int n) {
        std::unordered_set<int> antidiags, diags, cols;

        std::function<int(int)> dfs = [&](int row) -> int {
            if (row == n) {
                return 1;
            }
            int solutions = 0;
            for (int col = 0; col < n; ++col) {
                int cur_diag = row - col;
                int cur_anti_diag = row + col;
                if (cols.contains(col) || antidiags.contains(cur_anti_diag) || diags.contains(cur_diag)) {
                    continue;
                }
                cols.insert(col);
                diags.insert(cur_diag);
                antidiags.insert(cur_anti_diag);

                solutions += dfs(row + 1);

                cols.erase(col);
                diags.erase(cur_diag);
                antidiags.erase(cur_anti_diag);
            }
            return solutions;
        };
        return dfs(0);
    }
};

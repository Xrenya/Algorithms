class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int counter = 0;
        int ROWS = grid.size();
        int COLS = grid[0].size();
        std::vector<std::vector<int>> dirs = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };
        std::function<void(int, int)> dfs = [&](int row, int col) -> void {
            grid[row][col] = '0';
            for (int i = 0; i < dirs.size(); ++i) {
                int new_row = row + dirs[i][0];
                int new_col = col + dirs[i][1];
                if (new_row >= 0 && new_row < ROWS && new_col >= 0 && new_col < COLS && grid[new_row][new_col] == '1') {
                    dfs(new_row, new_col);
                }
            }
        };

        for (int i = 0; i < ROWS; ++i) {
            for (int j = 0; j < COLS; ++j) {
                if (grid[i][j] == '1') {
                    dfs(i, j);
                    ++counter;
                }
            }
        }

        return counter;
    }
};

class Solution {
public:
    int dfs(int row, int col, int ROWS, int COLS, vector<vector<int>>& grid) {
        if ((0 == row || row == ROWS - 1 || 0 == col || col == COLS - 1) && (grid[row][col] == 0 || grid[row][col] == 3)) {
            grid[row][col] = 3;
            return 0;
        } else if (0 < row && row < ROWS && 0 < col && col < COLS && grid[row][col] == 0) {
            grid[row][col] = 2;
            return dfs(row - 1, col, ROWS, COLS, grid) * dfs(row, col - 1, ROWS, COLS, grid) * dfs(row + 1, col, ROWS, COLS, grid) * dfs(row, col + 1, ROWS, COLS, grid);
        }
        return 1;
    }

    int closedIsland(vector<vector<int>>& grid) {
        int ROWS = grid.size(), COLS = grid[0].size(), count = 0;
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                if (grid[row][col] == 0) {
                    count += dfs(row, col, ROWS, COLS, grid);
                }
            }
        }
        // for (int row = 0; row < ROWS; row++) {
        //     for (int col = 0; col < COLS; col++) {
        //         std::cout << grid[row][col] << " ";
        //     }
        //     std::cout << std::endl;
        // }
        return count;
    }
};

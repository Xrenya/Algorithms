class Solution {
public:
    void dfs(int row, int col, int& ROWS, int& COLS, vector<vector<int>>& grid) {
      if (row < 0 || row > ROWS - 1 || col < 0 || col > COLS - 1) {
        return;
      } else if (grid[row][col] == 1) {
        grid[row][col] = 0;
        dfs(row + 1, col, ROWS, COLS, grid);
        dfs(row - 1, col, ROWS, COLS, grid);
        dfs(row, col + 1, ROWS, COLS, grid);
        dfs(row, col - 1, ROWS, COLS, grid);
        return;
      }
      return;
    }
    int numEnclaves(vector<vector<int>>& grid) {
      int ROWS = grid.size(), COLS = grid[0].size();
      for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLS; col++) {
          if ((row == 0 || col == 0 || row == ROWS - 1 || col == COLS - 1) &&grid[row][col] == 1) {
            dfs(row, col, ROWS, COLS, grid);
          }
        }
      }
      int count = 0;
      for (int row = 0; row < ROWS; row++) {
        for (int col = 0; col < COLS; col++) {
          if (grid[row][col]) {
              count++;
          }
        }
      }
      return count;
    }
};

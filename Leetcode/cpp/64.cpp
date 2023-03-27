class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
      int COLS = grid[0].size(), ROWS = grid.size();
      vector<vector<int>> mat(ROWS, vector<int>(COLS, -1));
      mat[0][0] = grid[0][0];
      // Fill the first row
      for (int col = 1; col < COLS; col++) {
        mat[0][col] = grid[0][col] + mat[0][col - 1];
      }
      // Fill the first col
      for (int row = 1; row < ROWS; row++) {
        mat[row][0] = grid[row][0] + mat[row - 1][0];
      } 
      // Fill the rest of the matrix
      for (int row = 1; row < ROWS; row++) {
        for (int col = 1; col < COLS; col++) {
          mat[row][col] = min(
            grid[row][col] + mat[row][col - 1], grid[row][col] + mat[row - 1][col]
          );
        } 
      }
      // Print matrix 
      // for (int row = 0; row < ROWS; row++) {
      //   for (int col = 0; col < COLS; col++) {
      //     std::cout << mat[row][col] << " ";
      //   } 
      //   std::cout << std::endl;
      // }
      return mat[ROWS - 1][COLS - 1];
    }
};
